import pygame
import time
import neat
import os
import pickle
from constants import FPS, HEIGHT, x1, y1, x2, y2
from pygame_functions import pygame_init, pygame_quit, Clock, pygame_display_image, check_esc
from functions import get_screen, image_to_file, jump
from image_processor2 import obstacle_distane_gameover

WIN = pygame_init()
time.sleep(10)
dinos_score = []
gen = 0


def main(genomes, config):
    global gen
    gen += 1
    print("generation ", gen)
    clock = Clock()
    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        g.fitness = 0
        run = True
        speed = 0
        obstacle_dist_prev = x2-x1

        time.sleep(0.5)
        jump(False)
        time.sleep(0.5)

        start = time.time()
        while run:
            screen = get_screen(x1, y1, x2, y2)
            pygame_display_image(WIN, image_to_file(screen), 0, 0)
            obstacle_dist, gameover, is_bird = obstacle_distane_gameover(
                WIN, screen)
            obstacle_dist = int(obstacle_dist)
            # print(obstacle_dist)
            if gameover:
                run = False
                break

            if obstacle_dist:
                if obstacle_dist < 90:
                    speed = int(abs(obstacle_dist_prev-obstacle_dist))
                    output = net.activate([obstacle_dist])
                    print(obstacle_dist, output)
                    if output[0] < 50:
                        jump(is_bird)
                        obstacle_dist_prev = x2-x1+speed

            # time.sleep(10)
            # print("gameover")
            # jump()
            # loop variables

            obstacle_dist_prev = obstacle_dist
            events = pygame.event.get()
           # pygame.display.update()
            #run = not pygame_quit(events) and not check_esc(events)
           # run = False
        end = time.time()
        time_elapsed = end-start
        print("time ", time_elapsed)
        g.fittness = int(time_elapsed)
        dinos_score.append(time_elapsed)
        # print("time", time_elapsed)
        if max(dinos_score) == time_elapsed:
            pickle.dump(net, open("best.pickle", "wb"))


def run(config_file):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_file)

    # Create the population, which is the top-level object f  or a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    # p.add_reporter(neat.StdOutReporter(True))
 #   stats = neat.StatisticsReporter()
 #   p.add_reporter(stats)
    # p.add_reporter(neat.Checkpointer(5))

    # Run for up to 50 generations.
    # fitness function
    axis = []

    winner = p.run(main, 500)
  #  with open("winner.pkl", "wb") as f:
  #      pickle.dump(winner, f)
  #      f.close()
# pygame#
 #   # show final stats
    print('\nBest genome:\n{!s}'.format(winner))


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    run(config_path)
