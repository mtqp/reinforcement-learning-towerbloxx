#coding=utf-8
from random import random

from environment import Environment

class Agent(object):
    def __init__(self, environment, kargs):
        self.environment = environment
        self.q_matrix = {}
        self.elegibilities = {}
        self.epsilon = kargs["epsilon"]
        self.alpha = kargs["alpha"]
        self.gamma = kargs["gamma"]
        print "Agent initialized with: epsilon: " + str(self.epsilon) + " alpha: "+ str(self.alpha) +" gamma: "+ str(self.gamma)
        
    def q_value(self, key):
        state,action = key
        return self.q_matrix.get((str(state),action), 0.0)

    def e_value(self,key):
        state,action = key
        return self.elegibilities.get((str(state),action),0.0)

    def set_q_value(self,(key),value):
        state,action = key
        old = self.q_matrix.get((str(state),action),"nfound")
        if  old == "nfound":
            self.environment.states_action_pair_count += 1
#            print str(state)
        self.q_matrix[(str(state),action)] = value

    def set_e_value(self,key,value):
        state,action = key
        self.elegibilities[(str(state),action)] = value

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

