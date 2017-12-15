from GA.Environment import Environment
from GA.Agent import Agent
import numpy as np

world = Environment()
world.population_init(10)

world.new_generation(4)
