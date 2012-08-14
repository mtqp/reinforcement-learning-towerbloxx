#coding=utf-8

import sys, pygame
#from towerbloxx import * 

HORIZONTAL = "horizontal"
VERTICAL = "vertical"


class UIObject(object):
    def __init__(self, image_path):
        self.surface = pygame.image.load(image_path)
        self.rectangle = self.surface.get_rect()
        self.name = image_path
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
        #self.images = images #ACA VA ALGO O QUE CARAJO?
        self.ui_objects = [UIObject("ball.bmp"), UIObject("warning.png")] #esto va a llevar una lista de las cosas q se carguen
        self.screen = pygame.display.set_mode(self.size)
        self.towerbloxx = towerbloxx #aca va a estar la interaccion con lo que efectivamente hay q visualizar

        #esto esta para testear
        self.ui_objects[0].set_speed(2,2)
        self.ui_objects[1].set_speed(5,6)
        
    def show(self):
        pygame.init()

        while 1:
            self._check_for_closure()

            for ui_object in self.ui_objects:
                ui_object.move()
                
                rect = ui_object.rectangle
                                
                if rect.left < 0 or rect.right > self.width:
                    ui_object.reverse_speed(HORIZONTAL)
                if rect.top < 0 or rect.bottom > self.height:
                    ui_object.reverse_speed(VERTICAL)

            self._refresh_screen()
            
    def _check_for_closure(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()

        
    def _refresh_screen(self):
        self.screen.fill(UI.BLACK)
        for ui_object in self.ui_objects:
            self.screen.blit(ui_object.surface, ui_object.rectangle)
        pygame.display.flip()
        
        
class Towerbloxx(object):
    def __init__(self, run_info):
        self.run_info = run_info
        
        
class RunInfo(object):
    def __init__(self, path):
        self.path = path
        self._load_info()
        
    def _load_info(self):
        print "implementar"
        

def main():

    run_info = RunInfo("dummyPath")
    towerbloxx = Towerbloxx(run_info)
    ui = UI(towerbloxx)
    
    ui.show()

if __name__ == "__main__":  
    main()
        
        
