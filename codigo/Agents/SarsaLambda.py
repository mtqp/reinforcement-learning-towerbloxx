
from copy import deepcopy

from Agent import *

class SarsaLambda(Agent):
    def __init__(self, lambda_val, environment):
        super(SarsaLambda, self).__init__(environment)
        self.lambda_val = lambda_val
        self.alpha = 0.4
        self.gamma = 0.8
        self.epsilon = 0.1

    def run_episode(self):
        state = self.environment.start()
        rewards = 0
        movements = 0
        action = self.choose_action(state) #usando una politica derivada de Q (eps-greedy en este caso)
                
        while not (state.has_finished() or movements > 100000):
            new_state, reward = self.environment.make_action(action)
            new_action = self.choose_action(new_state)
            delta = reward + self.gamma * self.q_value((new_state, new_action)) - self.q_value((state,action))
            self.elegibilities[(state,action)] = 1
            for (s,a) in self.q_matrix.keys():
                self.q_matrix[(s, a)] += self.alpha * delta * self.e_value((s,a))
                self.elegibilities[(s,a)] *= self.gamma * self.lambda_val

            state = deepcopy(new_state)
            action = new_action
            rewards += reward
            movements += 1
        
        return rewards
        
