import math
import random
import numpy as np

from sklearn import preprocessing
from game.Player import Player, Ball


class Game:
    canvas_width = 1000
    canvas_height = 700

    pheight = 100
    pwidth = 10
    speed = 4*12
    padd_color = (255,255,255)

    def __init__(self, p1, p2, pygame):
        self.p1 = p1
        self.p2 = p2
        self.player1 = Player(side=0, a=p1)
        self.player1.side = 1

        self.player2 = Player(side=0, a=p2)
        self.player2.side = 0

        self.ball = Ball()

        self.running = True
        self.pygame = pygame

        self.window = self.pygame.display.set_mode((self.canvas_width, self.canvas_height), 0, 32)
        self.myfont = self.pygame.font.SysFont("monospace", 45)


        self.fps = self.pygame.time.Clock()
        self.initialize_scene()

    def initialize_scene(self):
        self.player1.pos = 0.5 * self.canvas_height - 0.5 * self.pheight
        self.player2.pos = 0.5 * self.canvas_height - 0.5 * self.pheight
        self.ball.pos = (0.5 * self.canvas_width, 0.5 * self.canvas_height)




    def draw(self, canvas):
        canvas.fill((0, 0, 0))

        # check for collision
        ballx = self.ball.pos[0] + math.cos(self.ball.direction) * 8 + math.cos(self.ball.direction) * self.ball.speed
        bally = self.ball.pos[1] - math.sin(self.ball.direction) * 8 - math.sin(self.ball.direction) * self.ball.speed
        random_dir = (math.pi - self.ball.direction) + random.uniform(-1, 1) * (math.pi / 12)
        if ballx > self.canvas_width - self.pwidth and bally > self.player1.pos and bally < self.player1.pos + self.pheight:
            self.ball.direction = random_dir
        elif ballx < self.pwidth and bally > self.player2.pos and bally < self.player2.pos + self.pheight:
            self.ball.direction = random_dir
        elif bally < 5 or bally > self.canvas_height - 5:
            self.ball.direction = 270 - self.ball.direction + random.uniform(0,0.1)

        # update positions of paddles
        if self.player1.pos + self.player1.vel > 0 and self.player1.pos +self.player1.vel + self.pheight < self.canvas_height:
            if (self.player1.pos + self.player1.vel) > 0 and self.player1.vel > 0:
                self.player1.pos += self.player1.vel
            elif self.player1.pos + self.player1.vel + self.pheight < self.canvas_height and self.player1.vel < 0:
                self.player1.pos += self.player1.vel
            else:
                self.player1.pos += 0

        if self.player2.pos + self.player2.vel > 0 and self.player2.pos + self.player2.vel + self.pheight < self.canvas_height:
            if (self.player2.pos + self.player2.vel) > 0 and self.player2.vel > 0:
                self.player2.pos += self.player2.vel
            elif self.player2.pos + self.player2.vel + self.pheight < self.canvas_height and self.player2.vel < 0:
                self.player2.pos += self.player2.vel
            else:
                self.player2.pos += 0

        # update ball position
        self.ball.pos = (int(self.ball.pos[0] + math.cos(self.ball.direction) * self.ball.speed),int(self.ball.pos[1] - math.sin(self.ball.direction) * self.ball.speed))

        self.pygame.draw.rect(canvas, self.padd_color,
                         ((self.player1.side * self.canvas_width) - (self.player1.side * self.pwidth), self.player1.pos, self.pwidth, self.pheight))
        self.pygame.draw.rect(canvas, self.padd_color,
                         ((self.player2.side * self.canvas_width) - (self.player2.side * self.pwidth), self.player2.pos, self.pwidth, self.pheight))
        self.pygame.draw.circle(canvas, (180, 211, 53), self.ball.pos, 8)

        # check for win
        if self.ball.pos[0] > self.canvas_width:
            self.player2.score += 1
            self.restart()

        elif self.ball.pos[0] < 0:
            self.player1.score += 1
            self.restart()


        # update score
        label = self.myfont.render("%d" % (self.player1.score), 1, self.padd_color)
        label2 = self.myfont.render("%d" % (self.player2.score), 1, self.padd_color)
        canvas.blit(label, (0.5 * self.canvas_width + 50, 10))
        canvas.blit(label2, (0.5 * self.canvas_width - 50, 10))

    def move_player(self, p):
        # create movement of player

        features = np.array([self.ball.pos[0], self.ball.pos[1], p.pos, self.ball.direction, self.ball.speed])
        features_scaled = preprocessing.scale(features).reshape((1, 5))
        prediction = p.agent.ann.predict(features_scaled)

        will_move = prediction[0][0] > 0.5
        is_up = prediction[0][1] > 0.5
        move_event = None
        if will_move:

            if is_up:
                p.vel = -self.speed

            else:
                p.vel = self.speed

        else:
            p.vel = 0


    def restart(self):
        self.running = True
        self.window.fill((0, 0, 0))
        self.ball.speed = 4*15
        self.ball.pos = (0.5 * self.canvas_width, 0.5 * self.canvas_height)
        self.ball.direction = random.uniform(-1,1)*math.radians(45) + random.randint(0,1)*math.radians(180)
        self.player1.pos = 0.5 * self.canvas_height - 0.5 * self.pheight
        self.player2.pos = 0.5 * self.canvas_height - 0.5 * self.pheight
        self.draw(self.window)


    def update(self):
        if self.running:
            self.draw(self.window)

        if self.player1.is_AI:
            self.move_player(self.player1)


        if self.player2.is_AI:
            self.move_player(self.player2)

        self.pygame.display.update()
        self.fps.tick(60)








