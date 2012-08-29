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
    TITLE = "Towerbloxx Reinforcement Learning"
    BACKGROUND = 0
    CRANE = 1
    TOWER = 2
    COUNTER = 3
    REFRESH_SLOW = 1
    REFRESH_QUICK = 0.05
    WAIT = 3.5
    
    def __init__(self, towerbloxx):
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.size = self.width, self.height
        self.screen = pygame.display.set_mode(self.size)
        self.ui_objects = [UIBackground("background"), UICrane("crane"), UITower("tower"), UICounter("counter")] 
        self.towerbloxx = towerbloxx 
        pygame.display.set_caption(UI.TITLE)

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
                ui_tower.append_floor(floor)
                
                while not ui_tower.finished_dropping():
                    self._refresh_screen(UI.REFRESH_QUICK)
                
                self.ui_objects[UI.CRANE] = UICrane("next_crane")
            else:
                self._refresh_screen(UI.REFRESH_SLOW)

        self._show_final_screen()
        self.close()

    def _show_final_screen(self):
        counter = self._get_center_counter()
        background = self.ui_objects[UI.BACKGROUND]
        self.ui_objects = [background, counter]
        self._refresh_screen(UI.WAIT)

    def _get_center_counter(self):
        counter = self.ui_objects[UI.COUNTER]
        counter.place_center(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        return counter

    def update_state(self, state):
        for ui_object in self.ui_objects:
            ui_object.set_state(state)

    def _init_ui_objects(self, state):
        for ui_object in self.ui_objects:
            ui_object.start(state)

    def _refresh_screen(self, refresh_rate):
        for ui_object in self.ui_objects:
            ui_object.draw(self.screen)
        pygame.display.flip()
        time.sleep(refresh_rate)
        
    def _must_close(self):
        must_close = False
        for event in pygame.event.get():
            must_close |= event.type == pygame.QUIT
        return must_close

    def close(self):
        sys.exit()

        


