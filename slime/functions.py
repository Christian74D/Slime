from constants import SIDE, BLANK, CELL, e, ROWS, INVERSE_LAW_CONST
# main functions


def edit_grid(grid, mouse_pressed, mouse_pos):
    i, j, square = pos_to_square(grid, mouse_pos)
    if mouse_pressed[0]:  # left
        square.food = 1
        grid.foods[i][j] = 1
    elif mouse_pressed[2]:  # right
        square.food = 0
        grid.foods[i][j] = 0


def edit_grid2(grid, mouse_pressed, mouse_pos):
    i, j, square = pos_to_square(grid, mouse_pos)
    if mouse_pressed[0]:  # left
        square.slimed = 1
        grid.slimed[i][j] = 1
    elif mouse_pressed[2]:  # right
        square.slimed = 0
        grid.slimed[i][j] = 0


def pos_to_square(grid, mouse_pos):
    x, y = mouse_pos
    i = x // SIDE
    j = y // SIDE
    return i, j, grid.grid[i][j]


def calc_score(grid):
    foods = grid.foods
    score_mat = [[0]*ROWS for p in range(ROWS)]
    for i, rows in enumerate(foods):
        for j, food in enumerate(rows):
            if food:
                for x in range(ROWS):
                    for y in range(ROWS):
                        dist = calc_dist(i, j, x, y)
                        if dist:
                            score_mat[x][y] = score_mat[x][y] + \
                                1 / ((dist)**INVERSE_LAW_CONST)

                        #print(score_mat[1][1], score_mat[2][1])
                        #print(i, j, x, y, score_mat)
                """for x, row in enumerate(grid.grid):
                    for y, square in enumerate(row):
                        if((x, y) != (i, j)):

                            #square.score += func(calc_dist(i, j, x, y))
                            # print(square.score)"""
            # grid.grid[i][j].score = 1  # if food on cell score = 1
    total = 0
    for x in range(ROWS):  # finding avg
        for y in range(ROWS):
            total += score_mat[x][y]
    #avg = total / (ROWS*ROWS)
    # using list comphrehension to handle2d lists
    peaks = [max(p) for p in score_mat]
    peak = max(peaks)
   # print(score_mat)
  #  print(score_mat[1][1], score_mat[2][1])
    score_mat = [[q / peak for q in p] for p in score_mat]

    for x in range(ROWS):  # normalizing
        for y in range(ROWS):
            square = grid.grid[x][y]
            square.score = score_mat[x][y]  # / total  # * ROWS *ROWS
            """
            if(score_mat[x][y] != 0):  # to avoid zero error
                square.score = func1(score_mat[x][y])
            else:
                square.score = 1
            
            """
            # print(square.score)


def calc_dist(i, j, x, y):
    return ((i-x)**2 + (j-y)**2)**0.5


def func1(x):  # like sigmoid but x = 1/ input
    return 1/(1+e**(-x)) - 0.5  # only positive inputs


def func2(x):
    return
