import time
from constants import FPS, HEIGHT, x1, y1, x2, y2
from pygame_functions import pygame_init, pygame_quit, Clock, pygame_display_image, check_esc
from functions import get_screen, image_to_file, jump
from image_processor2 import obstacle_distane_gameover

#WIN = pygame_init()
time.sleep(10)


def main():
    #net = pickle.load(open("best_01.pickle", 'rb'))
    run = True
    while run:
        screen = get_screen(x1, y1, x2, y2)
        #pygame_display_image(WIN, image_to_file(screen), 0, 0)
        obstacle_dist, gameover, is_bird = obstacle_distane_gameover(
            "win", screen)
        if gameover:
            jump(False)
            run = False
            break

        if obstacle_dist:
           # speed = abs(obstacle_dist_prev-obstacle_dist)
           # output = net.activate([obstacle_dist, speed])
            if obstacle_dist < 80:
                jump(is_bird)

        # time.sleep(10)
        # print("gameover")
        # jump()
        # loop variables

    #events = pygame.event.get()
    # pygame.display.update()
    #run = not pygame_quit(events) and not check_esc(events)
    # run = False

    main()
    #g.fittness = time_elapsed
    #          dinos_score.append(time_elapsed)
    #print("time", time_elapsed)


main()
