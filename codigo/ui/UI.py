#coding=utf-8

import pygame, sys, time
from Towerbloxx import Towerbloxx
from UIObject import UIObject
from Constants import *

class UI(object):
    BLACK = 0,0,0
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    FLOOR = "imgs/floor.png"
    
    def __init__(self, towerbloxx):
        self.width = UI.SCREEN_WIDTH
        self.height = UI.SCREEN_HEIGHT
        self.size = self.width, self.height
        self.screen = pygame.display.set_mode(self.size)
        
        #esto va a llevar una lista de las cosas q se carguen
        self.ui_objects = [UIObject("crane", UI.FLOOR), UIObject("tower", UI.FLOOR)] 
        
        #aca va a estar la interaccion con lo que efectivamente hay q visualizar
        self.towerbloxx = towerbloxx 

    def show(self):
        pygame.init()
        
        init_state = self.towerbloxx.get_next_state()
        self._place_ui_objects(init_state)

        while self.towerbloxx.has_next_state():
            if self._must_close():
                self.close()
            state = self.towerbloxx.get_next_state()
            self._position_ui_objects(state)
            self._position_counter(state)
            self._refresh_screen()

        time.sleep(1.5)
        self.close()

    def close(self):
        sys.exit()
            
    def _place_ui_objects(self, state):
        crane_x, crane_y = self._parse_crane_position(state.crane)
        tower_x, tower_y = self._parse_tower_position(state.tower)

        ui_crane = self.ui_objects[0]
        ui_tower = self.ui_objects[1]
        ui_crane.place(crane_x, crane_y)
        ui_tower.place(tower_x, tower_y)
        
    def _parse_crane_position(self, crane_state):
        ui_crane = self.ui_objects[0]
        x_axis = self._get_x_axis(crane_state.position, ui_crane.get_width())
        y_axis = 0
        return x_axis, y_axis
        
    def _parse_tower_position(self, tower_state):
        ui_tower = self.ui_objects[1]
        x_axis = self._get_x_axis(tower_state.position, ui_tower.get_width())
        y_axis = UI.SCREEN_HEIGHT - ui_tower.get_height()
        return x_axis, y_axis

    def _get_x_axis(self, position, ui_width):
        shifted_position = position + 50
        x_axis = UI.SCREEN_WIDTH * shifted_position / 100
        x_axis = x_axis - (ui_width/2) #lo centra
        return x_axis

    def _set_crane_speed(self, state):
#       self.crane_direction = -1 #{-1;1}
#       self.crane_pos = -49 #[-49,49]
#       self.tower_vel = 0 #[-5,5]
#       self.tower_pos = 0 #[-49,49]
#       self.tower_height = 0
#       self.tower_factor = 0 #(-1,1)
#       self.tower_size = 10 #multiplos de 2

        ui_crane = self.ui_objects[0]
        ui_crane.horizontal_speed = state.crane.direction
    
    def _set_tower_speed(self, state):
        ui_tower = self.ui_objects[1]
        ui_tower.horizontal_speed = state.tower.speed
    
    def _position_counter(self, state):
        print "implementar position counter!!!!!"

    def _position_ui_objects(self, state):
        self._set_crane_speed(state)
        self._set_tower_speed(state)
        
        for ui_object in self.ui_objects:
            ui_object.move()
        
    def _refresh_screen(self):
        time.sleep(1)
        self.screen.fill(UI.BLACK)
        for ui_object in self.ui_objects:
            self.screen.blit(ui_object.surface, ui_object.rectangle)
        pygame.display.flip()
        
    def _must_close(self):
        must_close = False
        for event in pygame.event.get():
            must_close |= event.type == pygame.QUIT
        return must_close
