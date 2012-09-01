#coding=utf-8
import math
from ActionResolver.ActionResolver import *
from state import *

class Environment(object):

    MAX_HEIGHT = 3
    
    THROW = 1
    PASS = 0
    
    POSITION_BOUND = 49

    def initialize(self, crane_dir=-1, crane_pos=-49, tower_vel=0, tower_pos=0, 
                            tower_height=0, tower_factor=0, tower_size=10):
        self.crane_direction = crane_dir #{-1;1}
        self.crane_pos = crane_pos #[-49,49]
        self.tower_vel = tower_vel #[-5,5]
        self.tower_pos = tower_pos #[-49,49]
        self.tower_height = tower_height
        self.tower_factor = tower_factor #(-1,1)
        self.tower_size = tower_size #multiplos de 2
        self._finished = False

    def  __init__(self, **kwargs):
        self.initialize(**kwargs)

    def finish(self):
        self._finished = True

    def start(self):
        self.initialize()
        return self.state()

    def max_reward(self):
        return ActionResolver.MAX_REWARD

    def make_action(self, action):
        resolver = ActionResolver.create_for(self, action)
        reward = resolver.resolve()
        return self.state(), reward

    def add_floor(self):
        self.tower_height += 1
        if self.tower_height > self.MAX_HEIGHT:
            self.finish()
    
    def visible_factors(self):
        return self.tower_vel, self.tower_pos, self.crane_pos, self.crane_direction

    def state(self):
        return State(self)

    
