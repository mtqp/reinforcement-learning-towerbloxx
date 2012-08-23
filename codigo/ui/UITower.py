#coding=utf-8

from UIObject import UIObject
from UI import *
from Constants import *

class UITower(UIObject):
    def __init__(self, name):
        super(UITower, self).__init__(name, FLOOR_IMAGE + IMAGE_EXTENSION)
        
        
    def start(self, state):
        tower_x, tower_y = self._parse_tower_position(state.tower)
        super(UITower, self).place(tower_x, tower_y)

    def set_state(self, state):
        self.horizontal_speed = state.tower.speed * 10

    def draw(self, screen):
        super(UITower,self).move()
        screen.blit(self.surface, self.rectangle)
        
    def _parse_tower_position(self, tower_state):
        x_axis = self.get_x_axis(tower_state.position, super(UITower, self).get_width())
        y_axis = SCREEN_HEIGHT - super(UITower, self).get_height()
        return x_axis, y_axis
        
    def get_x_axis(self, position, ui_width):
        shifted_position = position + 50
        x_axis = SCREEN_WIDTH * shifted_position / 100
        x_axis = x_axis - (ui_width/2) #lo centra
        return x_axis

        
