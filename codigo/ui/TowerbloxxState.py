#coding=utf-8

class TowerbloxxState(object):
    def __init__(self, crane_state, tower_state):
        self.crane_state = crane_state
        self.tower_state = tower_state


class TowerState(object):
    def __init__(self, position, velocity, height, factor):
        self.position = position
        self.velocity = velocity
        self.height = height
        self.factor = factor
        
class CraneState(object):
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction



