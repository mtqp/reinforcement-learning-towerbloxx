#coding=utf-8

import pygame
from Constants import *

class UIObject(object):
    IMAGE_PATH = "imgs/"
    
    def __init__(self, name, image):
        self.surface = pygame.image.load(UIObject.IMAGE_PATH + image)
        self.rectangle = self.surface.get_rect()
        self.name = name
        self.horizontal_speed = 0
        self.vertical_speed = 0

    def set_image(self, image):
        bak_rectangle = self.rectangle
        self.surface = pygame.image.load(UIObject.IMAGE_PATH + image)
        self.rectangle = self.surface.get_rect()
        self.rectangle.top = bak_rectangle.top
        self.rectangle.left= bak_rectangle.left
              
    def get_height(self):
        return self.rectangle.bottom - self.rectangle.top
        
    def get_width(self):
        return self.rectangle.right - self.rectangle.left
                
    def set_speed(self, horizontal, vertical):
        self.horizontal_speed = horizontal
        self.vertical_speed = vertical
    
    def reverse_speed(self, direction):
        if direction == HORIZONTAL:
            self.horizontal_speed = -self.horizontal_speed
        else:
            self.vertical_speed = -self.vertical_speed
    
    def place(self, x_axis, y_axis):
        self.rectangle.left = x_axis
        self.rectangle.top = y_axis
    
    def move(self):
        speed = [self.horizontal_speed, self.vertical_speed]
        self.rectangle = self.rectangle.move(speed)
    

