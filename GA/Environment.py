import numpy as np
from GA.Agent import Agent
import random
import operator
import numpy as np
from Iter import Iter
import helpers
import itertools


class Environment:

    def __init__(self):
        self.population = []
        self.ancestry = []
        self.N = 0

    def population_init(self, num):
        for a in range(0, num):
            agent = Agent(generation=0)
            self.population.append(agent)
        self.N = len(self.population)

    def new_generation(self, num):
        new_population = []
        n = num

        best = self.select(self.fitness, n)

        # add all the best to next population
        for b in range(0, len(best)):
            new_population.append(best[b])

        # Choose offspring as direct cross over of best
        new_population.append(self.crossover(best[0], best[1]))

        # choose two random winners
        rand1 = random.randint(0,n-1)
        rand2 = random.randint(0,n-1)
        different = False
        while not different:
            rand2 = random.randint(0, n-1)
            if not(rand2 == rand1):
                different = True

        for i in range(0,3):
            new_population.append(self.crossover(best[rand1], best[rand2]))


        # add direct copy of two random winners
        rand1 = random.randint(0, n - 1)
        rand2 = random.randint(0, n - 1)
        new_population.append(best[rand1])
        new_population.append(best[rand2])

        self.ancestry.append(self.population)

        self.population = new_population
        self.mutate_population()

    def select(self, fitness, n):
        for a in range(0, self.N):
            self.population[a].fitness = fitness(self.population[a].score)
        self.population.sort(key=operator.attrgetter('fitness'), reverse=True)

        best = []
        for a in range(0, n):
            best.append(self.population[a])

        return best

    def crossover(self,a,b):
        # flatten out weight matrices for agent neural networks
        c = Agent(len(self.ancestry)+1)
        L = []

        # get array of size of weight matrices in weights list
        for l in range(0, len(a.ann.layer_size)-1):
            L.append((a.ann.layer_size[l]*(a.ann.layer_size[l+1]-1)) + sum(L))
        # create random crossover point
        random_crossover = random.randint(1, L[len(L)-1])
        for i in range(0,L[len(L)-1]):
            for j in range(0, len(L)):
                if i < (L[j]):
                    # calculate how many elmements into jth matrix in a_wr
                    k = i - sum(L[:j])

                    # go from jth element to rth row and cth column
                    row = k // (np.size(a.ann.layers[j].W, 1))
                    column = k % (np.size(a.ann.layers[j].W, 1))

                    if i < random_crossover:
                        c.ann.layers[j].W[row,column] = a.ann.layers[j].W[row,column]
                    else:
                        c.ann.layers[j].W[row,column] = b.ann.layers[j].W[row,column]
                    break
        return c

    def mutate(self, mutation_rate, a):
        rand = random.uniform(0, 1)

        for i in range(0, len(a.ann.layer_size)):
            for j in range(0, a.ann.layers[i].W.shape[0]):
                for k in range(0, a.ann.layers[i].W.shape[1]):
                    if rand < mutation_rate:
                        mutateFactor = 1 + ((random.uniform(0,1) - 0.5) * 3 + (random.uniform(0,1) - 0.5))
                        a.ann.layers[i].W[j, k] *= mutateFactor

        return a

    def mutate_population(self):
        for a in range(0, len(self.population)):
            self.population[a] = self.mutate(0.2, self.population[a])


    def fitness(self, score):
        # fitness function
        return score




