from Agent import *

class RMax(Agent):
    def __init__(self, environment):
        super(RMax, self).__init__(environment)
  
    def learn(self):
        for i in range(100):
            self.run_episode()
    
    def run_episode(self):
        pass