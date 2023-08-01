import numpy as np
import pygame
from constants import HEIGHT, GREY_1, GREY_2, WHITE, BLACK, xa, ya, xb, yb

# add function whentrasitioning from white to black and black to white


def obstacle_distane_gameover(win, screen):
    screen = np.array(screen)
    screen = np.delete(screen, [1, 2], axis=2)
    screen = np.resize(screen, (screen.shape[0], screen.shape[1]))
    obstacle_dist = find_obstacle_dist(win, screen)
    gameover = is_gameover(win, screen)
    is_bird = find_is_bird(screen, obstacle_dist)

    return obstacle_dist, gameover, is_bird


def find_is_bird(screen, obstacle_dist):
    for i in screen[HEIGHT-10, obstacle_dist:obstacle_dist+20]:
        if i == WHITE or i == BLACK:
            pass
        else:
            return False
    return True


def find_obstacle_dist(win, list):
    list_1 = np.flip(np.rot90(list), 0)
    bool_list_1 = (list_1 == GREY_1)

    result1 = np.where(bool_list_1)
    if len(result1[0]) != 0:
      #  pygame.draw.rect(win, (0, 255, 0), pygame.Rect(
        #  result[0][0]-2, 0, 4, HEIGHT))
        return result1[0][0]

    bool_list_2 = (list_1 == GREY_2)
    result2 = np.where(bool_list_2)
    if len(result2[0]) != 0:
      #  pygame.draw.rect(win, (0, 255, 0), pygame.Rect(
        #  result[0][0]-2, 0, 4, HEIGHT))
        return result2[0][0]

    else:
        return False


def is_gameover(win, screen):

    #pygame.draw.rect(win, (255, 0, 0), pygame.Rect(xa, ya, xb-xa, yb-ya))
    for i in screen[ya, xa:xb]:
        if i == GREY_1 or i == GREY_2:
            pass
        else:
            return False
    for i in screen[yb, xa:xb]:
        if i == GREY_1 or i == GREY_2:
            pass
        else:
            return False
    return True
