#coding=utf-8

import sys, pygame
#from towerbloxx import * 

class UI(object):
    def __init__(self, towerbloxx):
        self.width = 640
        self.height = 480
        self.speed = [2, 2]
        self.size = self.width, self.height
        #self.images = images #ACA VA ALGO O QUE CARAJO?
        self.images = pygame.image.load("ball.bmp") #esto va a llevar una lista de las cosas q se carguen
        self.screen = pygame.display.set_mode(self.size)
        self.towerbloxx = towerbloxx #aca va a estar la interaccion con lo que efectivamente hay q visualizar
        
    def show(self):
        black = 0,0,0
        
        pygame.init()

        images_rect = self.images.get_rect()

        while 1:
          for event in pygame.event.get():
              if event.type == pygame.QUIT: sys.exit()

          images_rect = images_rect.move(self.speed)
          if images_rect.left < 0 or images_rect.right > self.width:
              self.speed[0] = -self.speed[0]
          if images_rect.top < 0 or images_rect.bottom > self.height:
              self.speed[1] = -self.speed[1]

          self.screen.fill(black)
          self.screen.blit(self.images, images_rect)
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
        
        
