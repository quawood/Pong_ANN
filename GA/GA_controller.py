from GA.Environment import Environment
from game.Player import  Player
from game.Game import Game
import sys
import pygame

world = Environment()
world.population_init(10)

for g in range(0, 10):
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
                        world.population[j].score += new_game.player2.score
                        pygame.display.quit()
                        running = False
    world.new_generation(4)