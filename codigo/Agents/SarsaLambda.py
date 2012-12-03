
from copy import deepcopy

from Agent import *

class SarsaLambda(Agent):
    def __init__(self, environment, **args):
        super(SarsaLambda, self).__init__(environment, args)
        self.lambda_val = args["lambda_val"]

    def run_episode(self):
        state = self.environment.start()
        rewards = 0
        movements = 0
        action = self.choose_action(state) #usando una politica derivada de Q (eps-greedy en este caso)
                
        while not (state.has_finished() or movements > 300):
            new_state, reward = self.environment.make_action(action)
            new_action = self.choose_action(new_state)
            delta = reward + self.gamma * self.q_value((new_state, new_action)) - self.q_value((state,action))
            
            self.set_e_value((state,action),1.0)
            for k in self.elegibilities.keys():
                self.set_q_value(k, self.q_value(k) + self.alpha * delta * self.e_value(k))
                self.set_e_value(k, self.e_value(k) * self.gamma * self.lambda_val)

            state = deepcopy(new_state)
            action = new_action
            rewards += reward
            movements += 1
        return rewards
        
