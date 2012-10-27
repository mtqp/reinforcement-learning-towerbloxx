#coding=utf-8
from random import random

from environment import Environment

class Agent(object):
    def __init__(self, environment):
        self.environment = environment
        self.q_matrix = {}
        self.elegibilities = {}
        
    def q_value(self, state):
        return self.q_matrix.get(str(state), 0.0)

    def e_value(self,state):
        return self.elegibilities.get(str(state),0.0)

    def set_q_value(self,state,value):
        self.q_matrix[str(state)] = value

    def set_e_value(self,state,value):
        self.elegibilities[str(state)] = value

    def learn(self):
        for i in range(1000):
            self.run_episode()
            
    def choose_action(self, state):
        throw_val = self.q_value((state, Environment.THROW))
        pass_val = self.q_value((state, Environment.PASS))
        if throw_val > pass_val:
            action = Environment.THROW
            opposite_action = Environment.PASS
        elif throw_val < pass_val:
            action = Environment.PASS
            opposite_action = Environment.THROW
        else:
            coin = int(round(random()))
            action = Environment.THROW if coin else Environment.PASS
            return action
        
        return action if random() > self.epsilon else opposite_action

