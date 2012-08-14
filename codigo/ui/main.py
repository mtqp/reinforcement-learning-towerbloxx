#coding=utf-8

import sys, pygame
sys.path.append( "../" )
from environment import Environment
#from towerbloxx import * 

HORIZONTAL = "horizontal"
VERTICAL = "vertical"


class UIObject(object):
    def __init__(self, name, image_path):
        self.surface = pygame.image.load(image_path)
        self.rectangle = self.surface.get_rect()
        self.name = name
        self.horizontal_speed = 0
        self.vertical_speed = 0
                
    def set_speed(self, horizontal, vertical):
        self.horizontal_speed = horizontal
        self.vertical_speed = vertical
    
    def reverse_speed(self, direction):
        if direction == HORIZONTAL:
            self.horizontal_speed = -self.horizontal_speed
        else:
            self.vertical_speed = -self.vertical_speed
    
    def move(self):
        self.rectangle = self.rectangle.move([self.horizontal_speed, self.vertical_speed])
    

class UI(object):
    BLACK = 0,0,0
    
    def __init__(self, towerbloxx):
        self.width = 640
        self.height = 480
        self.size = self.width, self.height
        self.screen = pygame.display.set_mode(self.size)
        
        #esto va a llevar una lista de las cosas q se carguen
        self.ui_objects = [UIObject("ball", "ball.bmp"), UIObject("warning_sign", "warning.png")] 
        
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
            self.towerbloxx.set_next_state()

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

class TowerbloxxState(object):
    def __init__(self, crane_pos, tower_pos, action):
        self.crane_pos = crane_pos
        self.tower_pos = tower_pos
        self.action = action


class Towerbloxx(object):
    def __init__(self, run_info):
        self.run_info = run_info
        self._process_run_info()
        self.state = None
        
    def set_next_state(self):
        pass
        #print "implementar set_next_state"
        
    def _process_run_info(self):
        
        #------ESTOS VALORES SALEN DEL PROCESS -------
        crane_pos = 0
        tower_pos = 0
        action = Environment.PASS
        #---------------------------------------------
        self.state = TowerbloxxState(crane_pos, tower_pos, action)
        #pass
        print "implementar _process_run_info"
        
        
        
class RunInfo(object):
    def __init__(self, path):
        self.path = path
        self._load_info()
        
    def _load_info(self):
        pass
        #print "implementar _load_info"
        

def main():

    run_info = RunInfo("dummyPath")
    towerbloxx = Towerbloxx(run_info)
    ui = UI(towerbloxx)
    
    ui.show()

if __name__ == "__main__":  
    main()
        
        
