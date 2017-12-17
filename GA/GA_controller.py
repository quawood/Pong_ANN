from GA.Environment import Environment
from game.Game import Game
import pygame
import numpy as np
world = Environment()
world.population_init(10)

for g in range(0, 30):
    for i in range(0, len(world.population)):
        for j in range(0, len(world.population)):
            if not i == j:
                pygame.init()

                new_game = Game(world.population[i], world.population[j], pygame)
                running = True
                while running:
                    new_game.update()
                    if new_game.player1.score == 10 or new_game.player2.score == 10:
                        world.population[i].score += new_game.player1.score
                        pygame.display.quit()
                        running = False


    very_best = world.select(world.fitness(),1)
    W1 = very_best.ann.layers[0].W
    W2 = very_best.ann.layers[1].W

    with open('best_weights', 'w') as outfile:
        for data_slice in W1:
            # The formatting string indicates that I'm writing out
            # the values in left-justified columns 7 characters in width
            # with 2 decimal places.
            outfile.write('# Gen{0}\n'.format(g))
            np.savetxt(outfile, data_slice, fmt='%-7.2f')

            # Writing out a break to indicate different slices...

    with open('best_weights2', 'w') as outfile:
        for data_slice in W2:
            # The formatting string indicates that I'm writing out
            # the values in left-justified columns 7 characters in width
            # with 2 decimal places.
            outfile.write('# Gen{0}\n'.format(g))
            np.savetxt(outfile, data_slice, fmt='%-7.2f')

    world.new_generation(4)

