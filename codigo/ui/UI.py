#coding=utf-8

import pygame, sys, time
from Towerbloxx import Towerbloxx
from UIObject import UIObject
from UITower import UITower
from UICrane import UICrane
from UICounter import UICounter
from UIBackground import UIBackground
from Constants import *

class UI(object):
    CRANE = 1
    TOWER = 2
    COUNTER = 3
    REFRESH_SLOW = 1
    REFRESH_QUICK = 0.05
    WAIT = 10
    
    def __init__(self, towerbloxx):
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.size = self.width, self.height
        self.screen = pygame.display.set_mode(self.size)
        
        self.ui_objects = [UIBackground("background"), UICrane("crane"), UITower("tower"), UICounter("counter")] 
        self.towerbloxx = towerbloxx 

    def show(self):
        pygame.init()
        
        init_state = self.towerbloxx.get_next_state()
        self._init_ui_objects(init_state)

        while self.towerbloxx.has_next_state():
            if self._must_close():
                self.close()
            state = self.towerbloxx.get_next_state()
            self.update_state(state)

            if state.game.action == THROW:
                ui_tower = self.ui_objects[UI.TOWER]
                floor = self.ui_objects[UI.CRANE]
                ui_tower.append_floor(floor, state.game.reward)
                
                while not ui_tower.finished_dropping():
                    self._refresh_screen(UI.REFRESH_QUICK)
                
                self.ui_objects[UI.CRANE] = UICrane("next_crane")
            else:
                self._refresh_screen(UI.REFRESH_SLOW)

        time.sleep(UI.WAIT)
        self.close()

    def update_state(self, state):
        for ui_object in self.ui_objects:
            ui_object.set_state(state)

    def _init_ui_objects(self, state):
        for ui_object in self.ui_objects:
            ui_object.start(state)

    def _refresh_screen(self, refresh_rate):
        time.sleep(refresh_rate)
        for ui_object in self.ui_objects:
            ui_object.draw(self.screen)
        pygame.display.flip()
        
    def _must_close(self):
        must_close = False
        for event in pygame.event.get():
            must_close |= event.type == pygame.QUIT
        return must_close

    def close(self):
        sys.exit()

        


