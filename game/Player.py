import pygame, sys, time
from pygame.locals import *
import random
import math
class Player:
    is_AI = True
    side = 0
    score = 0
    pos = 0
    vel = 0
    def __init__(self, is_AI, side):
        self.is_AI = is_AI
        self.side = side



class Ball:
    pos = (0,0)
    speed = 0
    direction = 0

    def __init__(self):
        self.direction = random.randint(0,1)*math.radians(180)

        self.speed = 15

