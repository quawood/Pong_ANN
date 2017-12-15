from GA.Environment import Environment
from GA.Agent import Agent
from game.Player import  Player
import numpy as np
from game.game_controller import start_game

world = Environment()
world.population_init(10)



player1 = Player(side=0, a = world.population[0])
player2 = Player(side=1, a = world.population[0])

start_game(player1,player2)
