#coding=utf-8

import pygame
from Constants import *

class UIObject(object):
    def __init__(self, name, image_path):
        self.surface = pygame.image.load(image_path)
        self.rectangle = self.surface.get_rect()
        self.name = name
        self.horizontal_speed = 0
        self.vertical_speed = 0
                
    def set_speed(self, horizontal, vertical):
        self.horizontal_speed = horizontal
        self.vertical_speed = vertical
    
    def reverse_speed(self, direction):
        if direction == HORIZONTAL:
            self.horizontal_speed = -self.horizontal_speed
        else:
            self.vertical_speed = -self.vertical_speed
    
    def place(self, x_axis, y_axis):
        print "x_axis:" + str(x_axis)
        print "y_axis:" + str(y_axis)
        self.rectangle.left = x_axis
        self.rectangle.top = y_axis
    
    def move(self):
        print "moving hspeed:" + str(self.horizontal_speed) + "    vspeed:" + str(self.vertical_speed)
        self.rectangle = self.rectangle.move([self.horizontal_speed, self.vertical_speed])
    

