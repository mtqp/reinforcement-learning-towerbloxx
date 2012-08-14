#coding=utf-8

import sys, pygame
#from towerbloxx import * 

class UIObject(object):
    def __init__(self, image_path):
        self.surface = pygame.image.load(image_path)
        self.rect = self.surface.get_rect()
        self.name = image_path
        
    def name(self):
        return self.name

    def get_surface(self):
        return self.surface
        
    def get_rectangle(self):
        return self.rect
        
    def move(self, speed):
        self.rect = self.rect.move(speed)
    

class UI(object):
    BLACK = 0,0,0
    
    def __init__(self, towerbloxx):
        self.width = 640
        self.height = 480
        self.speed = [2, 2]
        self.size = self.width, self.height
        #self.images = images #ACA VA ALGO O QUE CARAJO?
        self.ui_objects = [UIObject("ball.bmp")] #esto va a llevar una lista de las cosas q se carguen
        self.screen = pygame.display.set_mode(self.size)
        self.towerbloxx = towerbloxx #aca va a estar la interaccion con lo que efectivamente hay q visualizar
        
    def show(self):
        pygame.init()

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            for ui_object in self.ui_objects:
                print "object " + ui_object.name
                print "speed " + str(self.speed)

                ui_object.move(self.speed)
                
                surface = ui_object.get_surface()
                rect = surface.get_rect()

                print "left " + str(rect.left)
                print "right " + str(rect.right)
                print "top " + str(rect.top)
                print "bottom " + str(rect.bottom)
                                
#               if rect.left <= 0 or rect.right >= self.width:
#                   self.speed[0] = -self.speed[0]
#               if rect.top <= 0 or rect.bottom >= self.height:
#                   self.speed[1] = -self.speed[1]

            self._refresh_screen()
            
        
    def _refresh_screen(self):
        self.screen.fill(UI.BLACK)
        for ui_object in self.ui_objects:
            surface = ui_object.get_surface()
            rect = ui_object.get_rectangle()
            self.screen.blit(surface, rect)
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
        
        
