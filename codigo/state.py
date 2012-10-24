#coding=utf-8

import math

def far_from_cero(f):
    if f<0:
        return int(math.floor(f))
    else:
        return int(math.ceil(f))


class State(object):
    def __init__(self, environment):
        self.environment = environment
        
    def __str__(self):
        return self.state_factors()
    
    def __cmp__(self, other):
        return cmp(str(self), str(other))

    def __hash__(self):
        return hash(str(self))

    def has_finished(self):
        return self.environment._finished
    
    def state_factors(self):
        factors = self.discretized_factors()
        return "TP {0}\tTV {1}\tCP {2}\tCD {3}".format(*factors)

    def discretized_factors(self):
        tower_pos = int(round(self.environment.tower_pos))
        tower_vel = far_from_cero(self.environment.tower_vel*10)
        crane_pos = self.environment.crane_pos
        crane_dir = self.environment.crane_direction
        return tower_pos, tower_vel, crane_pos, crane_dir
    
    def flat_factors(self):
        return self.environment.tower_pos, self.environment.tower_vel, self.environment.crane_pos, self.environment.crane_direction
        #rend 1 digito
        #*10 + redondear lejos de cero