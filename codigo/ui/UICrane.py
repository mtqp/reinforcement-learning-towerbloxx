#coding=utf-8

from UIObject import UIObject
from UI import *
from Constants import *

class UICrane(UIObject):
    def __init__(self, name):
        super(UIObject, self).__init__(name, FLOOR_IMAGE + IMAGE_EXTENSION)
        
    def start(self, state):
        crane_x, crane_y = self._parse_crane_position(state.crane)
        super(UIObject, self).place(crane_x, crane_y)

    def set_state(self, state):
        super(UIObject,self).horizontal_speed = state.crane.direction

    def draw(self, screen):
        super(UIObject,self).move()
        screen.blit(super(UIObject,self).ui_object.surface, super(UIObject,self).ui_object.rectangle)

    def _parse_crane_position(self, crane_state):
        x_axis = UI.get_x_axis(crane_state.position, super(UIObject, self).get_width())
        y_axis = 0
        return x_axis, y_axis
        
