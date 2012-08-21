#coding=utf-8

import pygame, sys, time
from Towerbloxx import Towerbloxx
from UIObject import UIObject
from Constants import *

class UI(object):
    BLACK = 0,0,0
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    
    def __init__(self, towerbloxx):
        self.width = UI.SCREEN_WIDTH
        self.height = UI.SCREEN_HEIGHT
        self.size = self.width, self.height
        self.screen = pygame.display.set_mode(self.size)
        
        #esto va a llevar una lista de las cosas q se carguen
        self.ui_objects = [UIObject("crane", "imgs/floor.png"), UIObject("tower", "imgs/floor.png")] 
        
        #aca va a estar la interaccion con lo que efectivamente hay q visualizar
        self.towerbloxx = towerbloxx 

    def show(self):
        pygame.init()
        
        #------esto esta para testear-----
        #self.ui_objects[0].set_speed(2,2)
        #self.ui_objects[1].set_speed(5,6)
        #---------------------------------
        init_state = self.towerbloxx.get_next_state()
        self._place_ui_objects(init_state)

        while self.towerbloxx.has_next_state() and not self._must_close():
            state = self.towerbloxx.get_next_state()
            self._position_ui_objects(state)
            self._refresh_screen()

        self.close()

    def close(self):
        time.sleep(1.5)
        sys.exit()
            
    def _place_ui_objects(self, state):
        ui_crane = self.ui_objects[0]
        ui_tower = self.ui_objects[1]
        
        crane_x, crane_y = self._parse_crane_position(state.crane)
        tower_x, tower_y = self._parse_tower_position(state.tower)

        ui_crane.place(0,0)#(crane_x, crane_y)
        ui_tower.place(0,123)#(tower_x, tower_y)
        
    def _parse_crane_position(self, crane_state):
        print "implementar parse crane position"
        return 0,0
        
    def _parse_tower_position(self, tower_state):
        print "implementar parse tower position"
        return 0,0

    ##ESTE LLEVA LA LOGICA CON EL TOWERBLOXX
    def _position_ui_objects(self, state):
        ui_crane = self.ui_objects[0]
        ui_tower = self.ui_objects[1]

        #ui_crane.set_speed(state.crane.direction, 0)
        #ui_tower.set_speed(state.tower.speed, 0)
        #no se xq se rompe si asigno solo una variable...
        #ui_crane.horizontal_speed = state.crane.direction
        #ui_tower.horizontal_speed = state.tower.speed
        
        for ui_object in self.ui_objects:
            ui_object.move()
            
#-----------esto esta para testear------------
#           rect = ui_object.rectangle
                            
#           if rect.left < 0 or rect.right > self.width:
#               ui_object.reverse_speed(HORIZONTAL)
#           if rect.top < 0 or rect.bottom > self.height:
#               ui_object.reverse_speed(VERTICAL)
#---------------------------------------------
        
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
