from GA.Environment import Environment
from game.Game import Game
from GA.Agent import Agent
import pygame
import numpy as np
world = Environment()
world.population_init(10)


def save_weights():
    W1 = []
    W2 = []
    best = world.select(world.fitness, 4)
    for b in range(0, len(best)):
        W1.append(best[b].ann.layers[0].W)
        W2.append(best[b].ann.layers[1].W)

    w = best[0].ann.layers[0].W.shape
    w2 = best[0].ann.layers[1].W.shape
    W1 = np.array(W1).reshape((4, w[0], w[1]))
    W2 = np.array(W2).reshape((4, w2[0], w2[1]))
    with open('best_weights.txt', 'wb') as outfile:
        # The formatting string indicates that I'm writing out
        # the values in left-justified columns 7 characters in width
        # with 2 decimal places.
        # outfile.write('# Gen1')
        for data_line in W1:
            np.savetxt(outfile, data_line, fmt='%-7.6f')
            outfile.write("# new\n".encode())

    with open('best_weights2.txt', 'wb') as outfile:
        # The formatting string indicates that I'm writing out
        # the values in left-justified columns 7 characters in width
        # with 2 decimal places.
        # outfile.write('# Gen1')
        for data_line in W2:
            np.savetxt(outfile, data_line, fmt='%-7.6f')
            outfile.write("# new\n".encode())


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


    # save weights of best agents of generation in text file
    save_weights()
    best = world.select(world.fitness, 4)
    print(g)
    world.new_generation(4, best)



