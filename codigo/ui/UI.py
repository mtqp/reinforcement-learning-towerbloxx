#coding=utf-8

import pygame, sys, time
from Towerbloxx import Towerbloxx
from UIObject import UIObject
from UITower import UITower
from UICrane import UICrane
from UICounter import UICounter
from Constants import *

class UI(object):
    BLACK = 0,0,0
    X_COUNTERS = 700    
    Y_COUNTERS = 400
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    CRANE = 0
    TOWER = 1
    COUNTER = 2
    
    def __init__(self, towerbloxx):
        self.width = UI.SCREEN_WIDTH
        self.height = UI.SCREEN_HEIGHT
        self.size = self.width, self.height
        self.screen = pygame.display.set_mode(self.size)
        
        self.ui_objects = [UICrane("crane"), UITower("tower"), UICounter("counter")] 
        self.towerbloxx = towerbloxx 

    def show(self):
        pygame.init()
        
        init_state = self.towerbloxx.get_next_state()
        self._init_ui_objects(init_state)

        #-----TESTING-
        i_counter = 0
        #-------------

        while self.towerbloxx.has_next_state():
            if self._must_close():
                self.close()
            state = self.towerbloxx.get_next_state()
        
            #-----TESTING-
            state.tower.height = i_counter
            i_counter += 1
            self.counter.set_state(state)
            #-------------
            self.update_state(state)
            self._refresh_screen()

        time.sleep(1.5)
        self.close()

    def update_state(self, state):
        for ui_object in self.ui_objects:
            ui_object.set_state(state)

    def close(self):
        sys.exit()
            
    def _init_ui_objects(self, state):
        for ui_object in self.ui_objects:
            ui_object.start(state)
        #crane_x, crane_y = self._parse_crane_position(state.crane)
        #tower_x, tower_y = self._parse_tower_position(state.tower)

        #ui_crane = self.ui_objects[UI.CRANE]
#        ui_tower = self.ui_objects[UI.TOWER]
 #       ui_counter=self.ui_objects[UI.COUNTER]
        
        #ui_crane.place(crane_x, crane_y)
  #      ui_tower.place(tower_x, tower_y)
   #     ui_counter.place(UI.X_COUNTERS, UI.Y_COUNTERS)

    def get_x_axis(self, position, ui_width):
        shifted_position = position + 50
        x_axis = UI.SCREEN_WIDTH * shifted_position / 100
        x_axis = x_axis - (ui_width/2) #lo centra
        return x_axis

    def _refresh_screen(self):
        time.sleep(1)
        self.screen.fill(UI.BLACK)
        for ui_object in self.ui_objects:
            ui_object.draw(self.screen)
        pygame.display.flip()
        
    def _must_close(self):
        must_close = False
        for event in pygame.event.get():
            must_close |= event.type == pygame.QUIT
        return must_close
        
         #   def _parse_crane_position(self, crane_state):
 #       ui_crane = self.ui_objects[UI.CRANE]
 #       x_axis = self._get_x_axis(crane_state.position, ui_crane.get_width())
 #       y_axis = 0
 #       return x_axis, y_axis
        
#   def _parse_tower_position(self, tower_state):
 #      ui_tower = self.ui_objects[UI.TOWER]
  #     x_axis = self._get_x_axis(tower_state.position, ui_tower.get_width())
   #    y_axis = UI.SCREEN_HEIGHT - ui_tower.get_height()
    #   return x_axis, y_axis


#   def _set_crane_speed(self, state):
#       self.crane_direction = -1 #{-1;1}
#       self.crane_pos = -49 #[-49,49]
#       self.tower_vel = 0 #[-5,5]
#       self.tower_pos = 0 #[-49,49]
#       self.tower_height = 0
#       self.tower_factor = 0 #(-1,1)
#       self.tower_size = 10 #multiplos de 2

#       ui_crane = self.ui_objects[UI.CRANE]
#       ui_crane.horizontal_speed = state.crane.direction
    
#   def _set_tower_speed(self, state):
#       ui_tower = self.ui_objects[UI.TOWER]
#       ui_tower.horizontal_speed = state.tower.speed

#   def _set_ui_objects(self, state):
#       self._set_crane_speed(state)
#       self._set_tower_speed(state)
#
#       for ui_object in self.ui_objects:
#           ui_object.move()

