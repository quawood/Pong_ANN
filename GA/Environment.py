import numpy as np
from GA.Agent import Agent
import random
import operator

class Environment:
    def __init(self):
        self.population = []
        self.ancestry = []
        self.N = len(self.population)


    def population_init(self, num):
        for a in range(0, num):
            agent = Agent(generation=0)
            self.population.append(agent)

    def new_generation(self, population, num):
        new_population = []
        n = num

        best = self.select(self.fitness, n)

        #add all the best to next population
        new_population.append(best)

        #Choose offspring as direct cross over of best
        new_population.append(self.crossover(best[0], best[1]))

        #choose two random winners
        rand1 = random.randint(0,n-1)
        rand2 = random.randint(0,n-1)
        different = False
        while not different:
            rand2 = random.randint(0, n-1)
            if not(rand2 == rand1):
                different = True

        for i in range(0,3):
            new_population.append(self.crossover(best[rand1], best[rand2]))


        #add direct copy of two random winners
        rand1 = random.randint(0, n - 1)
        rand2 = random.randint(0, n - 1)
        new_population.append(best[rand1])
        new_population.append(best[rand2])

        self.ancestry.append(population)
        self.population = new_population




    def select(self, fitness, n):
        for a in range(0, self.N):
            self.population[a].fitness = fitness(self.population[a].score)
        self.population.sort(key=operator.attrgetter('fitness'), reverse=True)

        best = []
        for a in range(0, n):
            best.append(self.population[a])

        return best


    def crossover(self,a,b):
        #flatten out weight matrices for agent neural networks
        a_weights = np.array([])
        b_weights = np.array([])

        for i in (0, a.ann.L):
            np.append(a_weights, (a.ann.layers[i].W.flatten()))
            np.append(b_weights, (b.ann.layers[i].W.flatten()))

        a_weights = a_weights.flatten()
        b_weights = b_weights.flatten()
        new_weights = np.ones((a_weights.shape))
        l = len(a_weights)

        #define random crossover point
        crossover_point = random.randint(1, l-2)
        for p in range(0,l):
            if p < crossover_point:
                new_weights[p] = a_weights[p]
            else:
                new_weights[p] = b_weights[p]

        c = Agent(0)
        for i in (0, a.ann.L):
            c.ann.layers[i].W = new_weights #Come back to this

        return c

    def mutate(self, mutation_rate, a):
        rand = random.uniform(0, 1)

        if random < mutation_rate:
            print("mutate a")
        return a


    def fitness(self, score):
        return score