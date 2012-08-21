#coding=utf-8

class TowerbloxxState(object):
    def __init__(self, crane_state, tower_state):
        self.crane = crane_state
        self.tower = tower_state


class TowerState(object):
    def __init__(self, position, speed, height, factor):
        self.position = position
        self.speed = speed
        self.height = height
        self.factor = factor
        
class CraneState(object):
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction



