import pygame
import random
from snowfall import *

class Snow():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(1, 3)
        self.img = random.randint(1, 3)
        self.img_name = str(self.img) + ".png"
        self.image = pygame.image.load(self.img_name).convert()
        self.image = pygame.transform.scale(self.image, (SNOW_SIZE, SNOW_SIZE))
    
    def move_snow(self):
        self.y += self.speed
        if self.y > MAX_Y:
            self.y = -SNOW_SIZE
        
        i = random.randint(1, 3)

        if i == 1:
            self.x += 1
            if self.x > MAX_X:
                self.x = -SNOW_SIZE
        elif i == 2:
            self.x -= 1
            if self.x < -SNOW_SIZE:
                self.x = MAX_X

    def draw_snow(self):
        screen.blit(self.image, (self.x, self.y))