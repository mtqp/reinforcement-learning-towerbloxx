#coding=utf-8

from UIObject import UIObject
from UI import *
from Constants import *

class UITower(UIObject):
    def __init__(self, name):
        super(UIObject, self).__init__(name, FLOOR_IMAGE + IMAGE_EXTENSION)
        
        
    def start(self, state):
        tower_x, tower_y = self._parse_tower_position(state.tower)
        super(UIObject, self).place(tower_x, tower_y)

    def set_state(self, state):
        super(UIObject,self).horizontal_speed = state.crane.direction

    def draw(self, screen):
        super(UIObject,self).move()
        screen.blit(super(UIObject,self).ui_object.surface, super(UIObject,self).ui_object.rectangle)
        
    def _parse_tower_position(self, tower_state):
        x_axis = UI.get_x_axis(tower_state.position, super(UIObject, self).get_width())
        y_axis = UI.SCREEN_HEIGHT - super(UIObject, self).get_height()
        return x_axis, y_axis
        
