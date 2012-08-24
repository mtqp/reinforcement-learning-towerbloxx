#coding=utf-8

import pygame
from Constants import *

class UIObject(object):
    IMAGE_PATH = "imgs/"
    
    def __init__(self, name, image):
        self.surface = pygame.image.load(UIObject.IMAGE_PATH + image)
        self.rectangle = self.surface.get_rect()
        self.name = name

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
                
    def place(self, x_axis, y_axis):
        self.rectangle.left = x_axis
        self.rectangle.top = y_axis
    
    def move_horizontally(self, y_axis):
        self.rectangle.top = self.rectangle.top + y_axis
       

