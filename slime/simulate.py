from constants import FPS, BLANK, CELL, THRESHOLD, SPREAD_MIN, SPREAD_MAX, ROWS, CHOKE_SHRINK, CHOKE_GROW
from grid import Grid
from functions import calc_score, edit_grid2
import pygame
import random


class Simulate:
    def __init__(self, win):
        self.grid = Grid(win)

    def draw(self):
        self.grid.draw()

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        run = False
                    if event.key == pygame.K_RETURN:
                        self.grow()

            self.update()
            self.draw()
            # clock.tick(FPS)

    def grow(self):
        run = True
        """for i in range(ROWS):
            for j in range(ROWS):
                self.grid.slimed[i][j] = self.grid.foods[i][j]"""
        for i in self.grid.foods:
            # self.grid.slimed[random.choice(
            #    range(ROWS))][random.choice(range(ROWS))] = 1
            self.grid.slimed[ROWS//2][ROWS//2] = 1
        clock = pygame.time.Clock()
        while run:
            self.grid.spread()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        run = False
                    if event.key == pygame.K_RETURN:
                        self.optimize()
                        run = False
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            edit_grid2(self.grid, mouse_pressed, mouse_pos)

            
            self.update()
            self.draw()
            # clock.tick(FPS)

    def optimize(self):
        run = 1
        while run:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.grid.optimize()
                        run = False
            for i in range(CHOKE_GROW):
                self.grid.spread()
                self.update()
                self.draw()
            for i in range(CHOKE_SHRINK):
                self.grid.optimize()
                self.update()
                self.draw()

    def update(self):
        grid = self.grid.grid
        calc_score(self.grid)

        for i in grid:
            for j in i:
                j.slimicity_update(random.uniform(SPREAD_MIN, SPREAD_MAX))

        new_grid = []

        for i in range(len(grid)):
            new_grid.append([])
            for j in range(len(grid[0])):
                score = self.grid.get_score(i, j)
                new_grid[-1].append(score - THRESHOLD)

        for i in grid:
            for j in i:
                j.slime = new_grid[j.x][j.y]  # try usin +="""

    def clear_grid(self):
        self.grid.clear()
