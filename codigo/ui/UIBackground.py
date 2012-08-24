#coding=utf-8

from UIObject import UIObject
from UI import *
from Constants import *
import math

class UIBackground(UIObject):
    FULL_RED = 255
    FULL_GREEN = 255
    NEUTRAL = 255, 255, 255

    def __init__(self, name):
        self.acum_rewards = 0
        self.color = UIBackground.NEUTRAL
        
    def start(self, state):
        pass

    def set_state(self, state):
        self.acum_rewards += state.game.reward
        self.color = self._get_background()

    def draw(self, screen):
        screen.fill(self.color)
        
    def _get_background(self):
        if -10 <= self.acum_rewards <= 10:
            return UIBackground.NEUTRAL
        else:
            percentage = self._get_percentage()
            if self.acum_rewards < 0:
                #go red
                red = UIBackground.FULL_RED
                red = math.ceil(red * percentage)
                return red,0,0
            else:
                #go green
                green = UIBackground.FULL_GREEN
                green = math.ceil(green * percentage)
                return 0,green,0
                
    def _get_percentage(self):
        mod_state = abs(self.acum_rewards)
        if mod_state > 2000:
            return 1.0
        elif mod_state > 1000:
                return 0.75
        elif mod_state > 500:
                return 0.5
        elif mod_state > 250:
                return 0.25
        else:
            return 0.10
