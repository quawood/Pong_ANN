import math
import random

import pygame
import sys
from pygame.locals import *

from game.Player import Player, Ball

import numpy as np
from game.key_test import Key_attr

key_attr = Key_attr()


def start_game(p1, p2):
    fps = pygame.time.Clock()
    canvas_width = 1000
    canvas_height = 500

    pheight = 150
    pwidth = 10
    speed = 12

    player1 = p1
    player1.side = 1
    player2 = p2
    player2.side = 0

    padd_color = (76, 163, 132)
    player1.pos = 0.5 * canvas_height - 0.5 * pheight
    player2.pos = 0.5 * canvas_height - 0.5 * pheight

    ball = Ball()
    ball.pos = (0.5 * canvas_width, 0.5 * canvas_height)

    pygame.init()

    window = pygame.display.set_mode((canvas_width, canvas_height), 0, 32)
    running = False
    myfont = pygame.font.SysFont("monospace", 45)

    # render text

    def draw(canvas, running):
        canvas.fill((0, 0, 0))

        # check for collision
        ballx = ball.pos[0] + math.cos(ball.direction) * 8 + math.cos(ball.direction) * ball.speed
        bally = ball.pos[1] - math.sin(ball.direction) * 8 - math.sin(ball.direction) * ball.speed
        random_dir = (math.pi - ball.direction) + random.uniform(-1, 1) * (math.pi / 12)
        if ballx > canvas_width - pwidth and bally > player1.pos and bally < player1.pos + pheight:
            ball.direction = random_dir
        elif ballx < pwidth and bally > player2.pos and bally < player2.pos + pheight:
            ball.direction = random_dir
        elif bally < 5 or bally > canvas_height - 5:
            ball.direction = 270 - ball.direction

        # update positions of paddles
        if player1.pos + player1.vel > 0 and player1.pos + player1.vel + pheight < canvas_height:
            if (player1.pos + player1.vel) > 0 and player1.vel > 0:
                player1.pos += player1.vel
            elif player1.pos + player1.vel + pheight < canvas_height and player1.vel < 0:
                player1.pos += player1.vel
            else:
                player1.pos += 0

        if player2.pos + player2.vel > 0 and player2.pos + player2.vel + pheight < canvas_height:
            if (player2.pos + player2.vel) > 0 and player2.vel > 0:
                player2.pos += player2.vel
            elif player2.pos + player2.vel + pheight < canvas_height and player2.vel < 0:
                player2.pos += player2.vel
            else:
                player2.pos += 0

        # update ball position
        ball.pos = (int(ball.pos[0] + math.cos(ball.direction) * ball.speed),
                    int(ball.pos[1] - math.sin(ball.direction) * ball.speed))

        pygame.draw.rect(canvas, padd_color,
                         ((player1.side * canvas_width) - (player1.side * pwidth), player1.pos, pwidth, pheight))
        pygame.draw.rect(canvas, padd_color,
                         ((player2.side * canvas_width) - (player2.side * pwidth), player2.pos, pwidth, pheight))
        pygame.draw.circle(canvas, (180, 211, 53), ball.pos, 8)

        still_running = running
        # check for win
        if ball.pos[0] > canvas_width:
            player2.score += 1
            still_running = False
        elif ball.pos[0] < 0:
            player1.score += 1
            still_running = False

        # update score
        label = myfont.render("%d" % (player1.score), 1, padd_color)
        label2 = myfont.render("%d" % (player2.score), 1, padd_color)
        canvas.blit(label, (0.5 * canvas_width + 50, 10))
        canvas.blit(label2, (0.5 * canvas_width - 50, 10))
        return still_running

    def keydown(event, running):
        still_running = running
        if event.key == K_UP:
            player1.vel = -speed
        elif event.key == K_DOWN:
            player1.vel = speed
        elif event.key == K_w:
            player2.vel = -speed
        elif event.key == K_s:
            player2.vel = speed
        elif event.key == K_r:
            if not running:
                restart()
        elif event.key == K_SPACE:
            if not running and ball.pos == (canvas_width * 0.5, canvas_height * 0.5):
                ball.speed = 15
                still_running = True

        return still_running

    def keyup(event):
        if event.key in (K_w, K_s):
            player2.vel = 0
        elif event.key in (K_UP, K_DOWN):
            player1.vel = 0

    def restart():

        window.fill((0, 0, 0))
        ball.speed = 0
        ball.pos = (0.5 * canvas_width, 0.5 * canvas_height)
        player1.pos = 0.5 * canvas_height - 0.5 * pheight
        player2.pos = 0.5 * canvas_height - 0.5 * pheight
        draw(window, running)

    while True:
        if running:
            running = draw(window, running)

        if player1.is_AI:

            features = np.array([ball.pos[0],ball.pos[1], player1.pos, ball.direction, ball.speed]).reshape((1,5))
            will_move = player1.agent.ann.predict(features)[0][0] > 0.99
            is_up = player1.agent.ann.predict(features)[0][1] > 0.99
            print(is_up)
            move_event = None
            if will_move:

                if is_up:
                    move_event = pygame.event.Event(KEYDOWN, Key_attr.UP)

                else:
                    move_event = pygame.event.Event(KEYDOWN, Key_attr.DOWN)

            else:
                if player2.vel < 0:
                    move_event = pygame.event.Event(KEYUP, [Key_attr.UP[1], Key_attr.UP[2]])
                else:
                    move_event = pygame.event.Event(KEYUP, [Key_attr.DOWN[1], Key_attr.DOWN[2]])

            pygame.event.post(move_event)

        if player2.is_AI:
            features = np.array([ball.pos[0], ball.pos[1], player1.pos, ball.direction, ball.speed]).reshape((1, 5))

            will_move = player2.agent.ann.predict(features)[0][0] > 0.5
            is_up = player2.agent.ann.predict(features)[0][1] > 0.5

            move_event = None
            if will_move:

                if is_up:
                    move_event = pygame.event.Event(KEYDOWN, Key_attr.w)

                else:
                    move_event = pygame.event.Event(KEYDOWN, Key_attr.s)

            else:
                if player2.vel < 0:
                    move_event = pygame.event.Event(KEYUP, [Key_attr.w[1], Key_attr.w[2]])
                else:
                    move_event = pygame.event.Event(KEYUP, [Key_attr.s[1], Key_attr.s[2]])

            pygame.event.post(move_event)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                running = keydown(event, running)
            elif event.type == KEYUP:
                keyup(event)

        pygame.display.update()
        fps.tick(60)
