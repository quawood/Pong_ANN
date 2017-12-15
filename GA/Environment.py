import numpy as np
from GA.Agent import Agent
import random
import operator
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
        #flatten out weight matrices for agent neural networks
        a_w = self.to_iter(a)
        b_w = self.to_iter(b)
        new_w = a_w
        L = self.get_max(a_w)
        random_crossover = random.randint(1, L - 2)
        for i in range(0,L):
            iterator = Iter(i)
            index = iterator.int_to_matrix(array=new_w)[1]
            if i < random_crossover:
                print(index)
                new_w[index[0]][index[1]][index[2]] = new_w[index[0]][index[1]][index[2]]
            else:
                new_w[index[0]][index[1]][index[2]] = b_w[index[0]][index[1]][index[2]]

        c = Agent(len(self.ancestry)+1)
        for i in range(0, a.ann.L):
            c.ann.layers[i].W = new_w[i]

        return c

    def mutate(self, mutation_rate, a):
        rand = random.uniform(0, 1)
        a_w = self.to_iter(a)

        #calculate legnth of flattened weights matrix
        L = self.get_max(a_w)
        for i in range(0, L):
            iterator = Iter(i)
            index = iterator.int_to_matrix(array=a_w)[1]
            if rand < mutation_rate:
                mutateFactor = 1 + ((random.uniform - 0.5) * 3 + (random.uniform - 0.5))
                a_w[index[0]][index[1]][index[2]] *= mutateFactor

        c = Agent(len(self.ancestry)+1)
        for i in range(0, a.ann.L):
            c.ann.layers[i].W = np.array(a_w[i])

        return c

    def mutate_population(self):
        for a in range(0, len(self.population)):
            self.population[a] = self.mutate(0.2, self.population[a])

    def fitness(self, score):
        #fitness function
        return score

    def to_iter(self, a):
        #returns multidimensional array with weight values of the network of agent a
        a_weights = []
        for i in range(0, a.ann.L-1):
            a_weights.append(a.ann.layers[i].W.tolist())

        a_w = a_weights
        return a_w

    def get_max(self, a):
        #return number of elements in weights array
        L = helpers._List_Amount(a)

        return L

