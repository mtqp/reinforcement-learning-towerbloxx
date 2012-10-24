
from copy import deepcopy

from Agent import *

class QAgent(Agent):
    def __init__(self, environment):
        super(QAgent, self).__init__(environment)
        self.alpha = 0.4
        self.gamma = 0.8
        self.epsilon = 0.1

    def max_action(self, state):
        throw_val = self.q_value((state, Environment.THROW))
        pass_val = self.q_value((state, Environment.PASS))
        if throw_val > pass_val:
            return Environment.THROW
        else:
            return Environment.PASS

    def run_episode(self):
        state = self.environment.start()
        rewards = 0
        movements = 0
        
        while not (state.has_finished()):
            
            action = self.choose_action(state) #usando una politica derivada de Q (eps-greedy en este caso)
            new_state, reward = self.environment.make_action(action)
            max_action = self.max_action(new_state)

            self.q_matrix[(state, action)] = (1-self.alpha)*self.q_value((state,action)) + self.alpha*(reward + self.gamma*self.q_value((new_state, max_action)))
            
            state = deepcopy(new_state)
            rewards += reward
            movements += 1
        print len(self.q_matrix.keys())
        return rewards        
        #f = open("datos_rewards.txt","a")
        #f.write(str(rewards)+"\n")
        #f.close()
        
