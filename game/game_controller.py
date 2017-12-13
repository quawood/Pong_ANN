import math
import random

import pygame
import sys
from pygame.locals import *

from game.Player import Player, Ball

fps = pygame.time.Clock()
canvas_width = 1000
canvas_height = 500

pheight = 150
pwidth = 10
speed = 12

player1 =  Player(is_AI=False, side=1)
player2 = Player(is_AI=False, side=0)
padd_color = (76, 163, 132)
player1.pos = 0.5*canvas_height - 0.5*pheight
player2.pos = 0.5*canvas_height - 0.5*pheight

ball = Ball()
ball.pos = (0.5*canvas_width, 0.5*canvas_height)

pygame.init()

window = pygame.display.set_mode((canvas_width,canvas_height), 0, 32)
running = False
myfont = pygame.font.SysFont("monospace", 45)

# render text

def draw(canvas, running):
    canvas.fill((0,0,0))

    #check for collision
    ballx = ball.pos[0] + math.cos(ball.direction)*8 + math.cos(ball.direction)*ball.speed
    bally = ball.pos[1] - math.sin(ball.direction)*8 - math.sin(ball.direction)*ball.speed
    random_dir = (math.pi - ball.direction) + random.uniform(-1, 1)*(math.pi/12)
    if ballx > canvas_width - pwidth and bally > player1.pos and bally < player1.pos + pheight:
        ball.direction = random_dir
    elif ballx < pwidth and bally > player2.pos and bally < player2.pos + pheight:
        ball.direction = random_dir
    elif bally < 5 or bally > canvas_height - 5:
        ball.direction = 270 - ball.direction


    #update positions of paddles
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
    ball.pos = (int(ball.pos[0] + math.cos(ball.direction)*ball.speed), int(ball.pos[1] - math.sin(ball.direction)*ball.speed))

    pygame.draw.rect(canvas, padd_color, ((player1.side * canvas_width) - (player1.side * pwidth), player1.pos, pwidth, pheight))
    pygame.draw.rect(canvas, padd_color, ((player2.side * canvas_width) - (player2.side * pwidth), player2.pos, pwidth, pheight))
    pygame.draw.circle(canvas, (180,211, 53), ball.pos, 8)





    still_running = running
    #check for win
    if ball.pos[0] > canvas_width:
        print("point for player 2")
        player2.score += 1
        still_running = False
    elif ball.pos[0] < 0:
        print("point for player 1")
        player1.score += 1
        still_running = False

    #update score
    label = myfont.render("%d" % (player1.score), 1, padd_color)
    label2 = myfont.render("%d" % (player2.score), 1, padd_color)
    canvas.blit(label, (0.5*canvas_width + 50, 10))
    canvas.blit(label2, (0.5*canvas_width - 50, 10))
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
        if not running and ball.pos == (canvas_width*0.5, canvas_height*0.5):
            ball.speed = 15
            still_running = True

    return  still_running

def keyup(event):
    if event.key in (K_w, K_s):
        player2.vel = 0
    elif event.key in (K_UP, K_DOWN):
        player1.vel = 0

def restart():

    window.fill((0, 0, 0))
    ball.speed = 0
    ball.pos = (0.5*canvas_width, 0.5*canvas_height)
    player1.pos = 0.5 * canvas_height - 0.5 * pheight
    player2.pos = 0.5 * canvas_height - 0.5 * pheight
    draw(window, running)

while True:
    if running:
        running = draw(window, running)

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