from ActionResolver import *

class PassActionResolver(ActionResolver):
    def reward(self):
    	if self.tower_fell():
            self.environment.finish()
            return self.TOWER_FELL_REWARD
        else:
        	return self.PASS_REWARD