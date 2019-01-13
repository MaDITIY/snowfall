import pygame
import random
import sys
import time

class Snow():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(1, 20)
        self.img = random.randint(1, 3)
        self.img_name = str(self.img) + ".png"
        self.image = pygame.image.load("img\\"+self.img_name).convert_alpha()
        self.image = pygame.transform.scale(self.image, (SNOW_SIZE, SNOW_SIZE))
    
    def move_snow(self):
        self.y += self.speed
        if self.y > MAX_Y:
            self.y = (0 - SNOW_SIZE)
        
        i = random.randint(1, 3)

        if i == 1:
            self.x += 1
            if self.x > MAX_X:
                self.x = (0 - SNOW_SIZE)
        elif i == 2:
            self.x -= 1
            if self.x < (0 - SNOW_SIZE):
                self.x = MAX_X

    def draw_snow(self):
        screen.blit(self.image, (self.x, self.y))

MAX_X = 1366
MAX_Y = 768
MAX_SNOW = 100
SNOW_SIZE = 100

game_over = False

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)#pygame.FULLSCREEN
bg_color = (0 , 0, 10)
snowfall = []

def initialize_snow(MAX_SNOW, SNOW_SIZE, snowfall):
    for i in range(0, MAX_SNOW):
        x = random.randint(0, MAX_X - SNOW_SIZE)
        y = 0
        snowfall.append(Snow(x, y))    

initialize_snow(MAX_SNOW, SNOW_SIZE, snowfall)

while game_over == False :
    screen.fill(bg_color)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            game_over = True
    for i in snowfall:
        i.move_snow()
        i.draw_snow()
    time.sleep(0.02)
    pygame.display.flip()