from ActionResolver import *

class PassActionResolver(ActionResolver):
    def reward(self):
        return self.PASS_REWARD