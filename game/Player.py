import pygame, sys, time
from pygame.locals import *
import random
import math
from GA.Agent import Agent

class Player:

    def __init__(self,side, a=None):
        if isinstance(a, Agent):
            self.is_AI = True
            self.agent = a
        self.side = side
        self.score = 0
        self.pos = 0
        self.vel = 0


class Ball:
    pos = (0,0)
    speed = 0
    direction = 0

    def __init__(self):
        self.direction = random.randint(0,1)*math.radians(180)

        self.speed = 15

