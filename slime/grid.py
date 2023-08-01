import pygame
from square import Square
import random
from constants import CELL, HEIGHT, ROWS, BLANK, SLIME, CELL, BORDER_WIDTH, BORDER_COLOR, SPREAD_MIN, SPREAD_MAX, CELL_COUNT, OPTIM_MIN, OPTIM_MAX, OPTIM_SPEED


class Grid:
    def __init__(self, win):
        self.win = win
        self.height = self.width = HEIGHT
        self.rows = self.cols = ROWS
        self.side = HEIGHT // ROWS
        self.foods = []
        self.slimed = [[0]*ROWS for p in range(ROWS)]
        self.grid = self.make_grid()
        self.found_food = [[0]*ROWS for p in range(ROWS)]

    def make_grid(self):
        grid = []
        for i in range(self.rows):
            self.foods.append([])
            grid.append([])
            for j in range(self.cols):
                sq = Square(self.win, i,
                            j, self.side, SLIME)
                sq.slimicity_update(random.uniform(SPREAD_MIN, SPREAD_MAX))
                self.foods[i].append(0)
                grid[i].append(sq)
        return grid

    def draw_borders(self):
        for i in range(self.rows+1):
            pygame.draw.rect(self.win, BORDER_COLOR, (0, i*self.side -
                             BORDER_WIDTH/2, self.width, BORDER_WIDTH))

        for j in range(self.cols+1):
            pygame.draw.rect(self.win, BORDER_COLOR, (j*self.side -
                             BORDER_WIDTH/2, 0, BORDER_WIDTH, self.height))

    def draw_squares(self):
        for i in self.grid:
            for j in i:
                j.draw()

    def clear(self):
        self.grid = self.make_grid

    def draw(self):
        self.win.fill(BLANK)
        self.draw_squares()
        self.draw_borders()
        pygame.display.update()

    def spread(self):
        slimed = [[0]*ROWS for p in range(ROWS)]
        for i in range(ROWS):
            for j in range(ROWS):
                slimed[i][j] = self.slimed[i][j]

        for i, row in enumerate(slimed):
            for j, val in enumerate(row):
                if val:
                    cells = self.get_neighbours(self.grid[i][j])
                    count = 0
                    for cell in cells:
                        count += cell.slimed
                    if(count < CELL_COUNT):
                        max_slime = 0  # finding cell with max score
                        max_cell = self.grid[i][j]
                        for cell in cells:
                            if (cell.slime > max_slime and cell.slimed == 0):
                                max_slime = cell.slime
                                max_cell = cell

                        max_cell.slimed = 1
                        self.slimed[max_cell.x][max_cell.y] = 1

    def connect(self, cell):
        cells = self.get_neighbours(cell)
        if cell.food:
            self.found_food[cell.x][cell.y] = 1
        for i in cells:
            if (i.slimed or i.food) and not i.found:
                i.found = 1
                #print(i.x, i.y)
                self.connect(i)

    def check_connected(self):
        for x in range(ROWS):  # finding start cell
            for y in range(ROWS):
                self.grid[x][y].found = 0
                self.found_food[x][y] = 0

        for x in range(ROWS):  # finding start cell
            for y in range(ROWS):
                if self.grid[x][y].food:
                    cell = self.grid[x][y]
                    break
        self.connect(cell)
        return (self.found_food == self.foods)

    def optimize(self):
        for i in range(OPTIM_SPEED):
            x = random.randint(0, ROWS - 1)
            y = random.randint(0, ROWS - 1)
            if (self.grid[x][y].slimed):
                self.grid[x][y].slimed = 0
                self.slimed[x][y] = 0
                connected = self.check_connected()
                # print(connected)
                if(not connected):  # if disonnects dont disconnect
                    self.grid[x][y].slimed = 1
                    self.slimed[x][y] = 1

    def get_score(self, i, j):
        cells = self.get_neighbours(self.grid[i][j])
        score = 0
        for k in cells:
            score += k.slime

        return score / len(cells)

    def get_neighbours(self, node):
        x, y = node.x, node.y
        cells = []
        up = y > 0
        right = x < len(self.grid[0])-1
        down = y < len(self.grid)-1
        left = x > 0

        if up:
            cells.append(self.grid[x][y-1])
        if right:
            cells.append(self.grid[x+1][y])
        if down:
            cells.append(self.grid[x][y+1])
        if left:
            cells.append(self.grid[x-1][y])

        if up and right:
            cells.append(self.grid[x+1][y-1])
        if down and right:
            cells.append(self.grid[x+1][y+1])
        if down and left:
            cells.append(self.grid[x-1][y+1])
        if up and left:
            cells.append(self.grid[x-1][y-1])

        cells.append(self.grid[x][y])
        return cells
