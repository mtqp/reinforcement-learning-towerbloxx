#coding=utf-8
import math
from ActionResolver.ActionResolver import *
from state import *

def far_from_cero(f):
    if f<0:
        return int(math.floor(f))
    else:
        return int(math.ceil(f))

class Environment(object):

    THROW = 1
    PASS = 0

    INITIAL_CRANE_POS = -49
    
    POSITION_BOUND = 49

    def __str__(self):
        factors = self.discretized_factors()
        return "TP {0}\tTV {1}\tCP {2}\tCD {3}".format(*factors)
    
    def discretized_factors(self):
        tower_pos = int(round(self.tower_pos))
        tower_vel = far_from_cero(self.tower_vel)
        crane_pos = self.crane_pos
        crane_dir = self.crane_direction
        return tower_pos, tower_vel, crane_pos, crane_dir
    
    def initialize(self):
        self.crane_direction = self.args.get('crane_dir') or 1 
        self.crane_pos = self.args.get('crane_pos') or self.INITIAL_CRANE_POS
        self.tower_vel = self.args.get('tower_vel') or 0
        self.tower_pos = self.args.get('tower_pos') or 0
        self.tower_height = self.args.get('tower_height') or 20
        self.max_height = self.args.get('max_height') or 60
        self.tower_size = self.args.get('tower_size') or 10
        self.tower_angle = self.args.get('tower_angle') or 0
        self._finished = False

    def  __init__(self, **args):
        self.args = args
        self.initialize()
        self.states_action_pair_count = 0

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
        if self.tower_height >= self.max_height:
            self.finish()
        else:
            self.crane_dir = 1
            self.crane_pos = self.INITIAL_CRANE_POS

    def state(self):
        return State(self)


    
