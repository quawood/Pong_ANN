import pygame
from pygame.locals import *
import sys
# pygame.init()
# window = pygame.display.set_mode((500, 500), 0, 32)
#
# #
# # def keydown(event):
# #     print((event.unicode, event.key, event.mod))
# #
# #
# # def keyup(event):
# #     print((event.key, event.mod))
# #
# #
# #
# # while True:
# #     for event in pygame.event.get():
# #         if event.type == QUIT:
# #             pygame.quit()
# #             sys.exit()
# #         elif event.type == KEYDOWN:
# #             keydown(event)
# #         elif event.type == KEYUP:
# #             keyup(event)
# #
# #
# #

class Key_attr:
    UP = {'unicode': '\uf700', 'key': 273, 'mod': 0}
    DOWN = {'unicode': '\uf701', 'key': 274, 'mod': 0}
    w = {'unicode': 'w', 'key': 119, 'mod': 0}
    s = {'unicode': 's', 'key': 115, 'mod': 0}


    def __init__(self):
        print("initialized")
