#coding=utf-8

from UIObject import UIObject
from UI import *
from Constants import *

class UICrane(UIObject):
    def __init__(self, name):
        super(UICrane, self).__init__(name, FLOOR_IMAGE + IMAGE_EXTENSION)
        
    def start(self, state):
        crane_x, crane_y = self._parse_crane_position(state.crane)
        super(UICrane, self).place(crane_x, crane_y)

    def set_state(self, state):
        self.horizontal_speed = state.crane.direction * 10

    def draw(self, screen):
        super(UICrane,self).move()
        screen.blit(self.surface, self.rectangle)

    def _parse_crane_position(self, crane_state):
        x_axis = self.get_x_axis(crane_state.position, super(UICrane, self).get_width())
        y_axis = 0
        return x_axis, y_axis
        
    def get_x_axis(self, position, ui_width):
        shifted_position = position + 50
        x_axis = SCREEN_WIDTH * shifted_position / 100
        x_axis = x_axis - (ui_width/2) #lo centra
        return x_axis

        
