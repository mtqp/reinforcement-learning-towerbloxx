#coding=utf-8
import math
from ActionResolver.ActionResolver import *
from state import *

class Environment(object):

    MAX_HEIGHT = 10
    
    THROW = 1
    PASS = 0
    
    POSITION_BOUND = 49

    def initialize(self):
        self.crane_direction = -1 #{-1;1}
        self.crane_pos = -49 #[-49,49]
        self.tower_vel = 0 #[-5,5]
        self.tower_pos = 0 #[-49,49]
        self.tower_height = 0
        self.tower_factor = 0 #(-1,1)
        self.tower_size = 10 #multiplos de 2

    def  __init__(self):
        self.initialize()

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
            self.state().finish()
    
    def visible_factors(self):
        return self.tower_vel, self.tower_pos, self.crane_pos, self.crane_direction

    def state(self):
        return State(self)

    
