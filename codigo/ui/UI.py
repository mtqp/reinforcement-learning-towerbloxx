#coding=utf-8

import pygame
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
        self.ui_objects[0].set_speed(2,2)
        self.ui_objects[1].set_speed(5,6)
        #---------------------------------

        while 1:
            if self._must_close():
                self.close()
            self._position_ui_objects()
            self._refresh_screen()
            #state = self.towerbloxx.get_next_state()

    def close(self):
        sys.exit()
            
    ##ESTE LLEVA LA LOGICA CON EL TOWERBLOXX
    def _position_ui_objects(self):
        for ui_object in self.ui_objects:
            ui_object.move()
            
            rect = ui_object.rectangle
                            
            if rect.left < 0 or rect.right > self.width:
                ui_object.reverse_speed(HORIZONTAL)
            if rect.top < 0 or rect.bottom > self.height:
                ui_object.reverse_speed(VERTICAL)
        
    def _refresh_screen(self):
        self.screen.fill(UI.BLACK)
        for ui_object in self.ui_objects:
            self.screen.blit(ui_object.surface, ui_object.rectangle)
        pygame.display.flip()
        
    def _must_close(self):
        must_close = False
        for event in pygame.event.get():
            must_close |= event.type == pygame.QUIT
        return must_close
