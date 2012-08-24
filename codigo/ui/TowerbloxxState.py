#coding=utf-8

class TowerbloxxState(object):
    def __init__(self, crane_state, tower_state, game_state):
        self.crane = crane_state
        self.tower = tower_state
        self.game  = game_state

class TowerState(object):
    def __init__(self, position, height, factor):
        self.position = position
        self.height = height
        self.factor = factor
        
class CraneState(object):
    def __init__(self, position):
        self.position = position

class GameState(object):
    def __init__(self, action, reward):
        self.action = action
        self.reward = reward



