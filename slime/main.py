import pygame
from constants import WIDTH, HEIGHT, ROWS, CAPTION, FPS
from functions import edit_grid
from simulate import Simulate

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)


def main():

    game = Simulate(WIN)
    run = True

    while run:
        game.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game.run()
                if event.key == pygame.K_BACKSPACE:
                    game = Simulate(WIN)

        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        edit_grid(game.grid, mouse_pressed, mouse_pos)


main()
