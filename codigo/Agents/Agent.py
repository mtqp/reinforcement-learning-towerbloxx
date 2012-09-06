#coding=utf-8
from random import random

from environment import Environment

class Agent(object):
    def __init__(self, environment, episodes):
        self.environment = environment
        self.episodes = episodes
        
    def q_value(self, key):
        s,a = key
        s = s.state_factors()
        return self.q_matrix.get((s,a), 0)

    def set_q_value(self, key, value):
        s,a = key
        s = s.state_factors()
        self.q_matrix[(s,a)] = value

    def e_value(self,key):
        s,a = key
        s = s.state_factors()
        return self.elegibilities.get((s,a),0)

    def set_elegibility(self,key, value):
        s,a = key
        s = s.state_factors()
        self.elegibilities[(s,a)] = value
    
    def learn(self):
        for i in range(self.episodes):
            self.run_episode(i == self.episodes-1)
            
    def choose_action(self, state):
        throw_val = self.q_value((state, Environment.THROW))
        pass_val = self.q_value((state, Environment.PASS))
        if throw_val >= pass_val:
            action = Environment.THROW
            opposite_action = Environment.PASS
        else:
            action = Environment.PASS
            opposite_action = Environment.THROW
        
        return action if random() > self.epsilon else opposite_action

    def what_did_i_learned(self):
        pass
        #print "#of States: " + str(len(self.q_matrix.keys()))
