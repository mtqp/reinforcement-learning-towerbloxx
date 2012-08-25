from Agent import *

class QAgent(Agent):
    def __init__(self, environment):
        super(QAgent, self).__init__(environment)
        self.q_matrix = {}
        self.alpha = 0.5
        self.gamma = 0.9
        self.epsilon = 0.1
    
    def qvalue(self, key):
        return self.q_matrix.get(key, 0)
    
    def learn(self):
        for i in range(100):
            self.run_episode()
    
    def run_episode(self):
        state = self.environment.start()
        while not state.has_finished():
            action = self.choose_action(state)
            new_state, reward = self.environment.make_action(action)
            prev_qvalue = self.qvalue((state, action))
            self.q_matrix[(state, action)] = prev_qvalue + self.alpha * (
                reward + self.gamma * self.max_action(new_state) - prev_qvalue)
            state = new_state
    
    def max_action(self, state):
        throw_val = self.qvalue((state, Environment.THROW))
        pass_val = self.qvalue((state, Environment.PASS))
        return max(throw_val, pass_val)
    
    def choose_action(self, state):
        throw_val = self.qvalue((state, Environment.THROW))
        pass_val = self.qvalue((state, Environment.PASS))
        if throw_val >= pass_val:
            action = Environment.THROW
            opposite_action = Environment.PASS
        else:
            action = Environment.PASS
            opposite_action = Environment.THROW
        
        return action if random() > self.epsilon else opposite_action