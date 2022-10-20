import pygame
from vector import Vector
from helpers import *
import random
from pygame.locals import(RLEACCEL)
import math

# randomn seed
#random.seed(random_seed)

class ModelObject(pygame.sprite.Sprite):
    def __init__(self, sprite_path="",offset=10):
        super(ModelObject, self).__init__()
        #load sprite img
        self.surf = pygame.image.load(sprite_path).convert_alpha()
        self.surf.set_colorkey(WHITE, RLEACCEL)
        self.rect = self.surf.get_rect()
        self.position = Vector()
        self.offset = offset
        self.position.randomize(SCREEN_DIMENSION-self.offset)
        self.rotation = random.random() * math.pi
        self.direction = Vector(math.cos(self.rotation), math.sin(self.rotation))
        self.speed = 0.0
    
    # rotate the object  
    def rotate(self, rad=0.0, clockwise=True):
        if rad == 0.0:
            return
        if clockwise:
            self.rotation += rad
        else:
            self.rotation -= rad
        # rotate the vector
        self.direction = Vector(math.cos(self.rotation), math.sin(self.rotation))
    
    # move the object
    def move(self, speed=0, limit=SCREEN_DIMENSION):
        new_pos = self.position.add(self.direction.scalar_mult(speed * DELTA_TIME))
        
         # x limits
        if new_pos.x < self.offset or new_pos.x > (limit-self.offset):
            new_pos.x = self.position.x
        # y limits
        if new_pos.y < self.offset or new_pos.y > (limit-self.offset):
            new_pos.y = self.position.y

        self.position = new_pos
    
    def set_direction(self, rad=0.0):
        self.rotation = rad
        self.direction = Vector(math.cos(self.rotation), math.sin(self.rotation))
        
    
        