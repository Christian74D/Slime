import pygame
from constants import WIDTH, HEIGHT, CAPTION


def pygame_init():
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(CAPTION)

    return WIN


def Clock():
    return pygame.time.Clock()


def pygame_quit(events):
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            return True


def pygame_display_image(win, image_name, x, y):
    image = pygame.image.load(image_name)
    win.blit(image, (x, y))


def check_esc(events):
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return True
    else:
        return False
