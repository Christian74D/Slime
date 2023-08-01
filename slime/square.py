import pygame
from constants import ROWS, FOOD, ORANGE, SLIME, SLIMED


class Square:
    def __init__(self, win, x, y, side, color):
        self.win = win
        self.x = x
        self.y = y
        self.side = side
        self.color = color
        self.f_color = color
        self.slime = 0
        self.slimed = 0
        self.food = 0
        self.score = 0
        self.active = 1
        self.found = 0

    def slimicity_update(self, slime):  # slime val bet 0 and 1
        self.slime = slime

    def draw(self):
        # updating slime
        # self.slime * self.score  # slime / score mode conv
        slime = max(min(self.slime + self.score, 1), 0)
        self.slime = slime
        # print(self.score)
        self.color = SLIME
        self.color = (
            rgb(self.color[0]*slime), rgb(self.color[1] * slime), rgb(self.color[2]*slime))

        if(self.food):  # if food change color
            self.f_color = FOOD
        elif(self.slimed):
            self.f_color = SLIMED
        else:
            self.f_color = self.color
        # print(self.f_color)
        pygame.draw.rect(self.win, self.f_color, (
            self.x*self.side, self.y*self.side, self.side, self.side))


def rgb(color):
    return max(min(color, 255), 0)
