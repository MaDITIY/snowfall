import pygame
import random
from snow import Snow

MAX_X = 1366
MAX_Y = 768
MAX_SNOW = 100
SNOW_SIZE = 64

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
bg_color = (0,0,10)

initialize_snow(MAX_SNOW, SNOW_SIZE)

while True:
    check_exit()
    Snow.move_snow()
    Snow.draw_snow()