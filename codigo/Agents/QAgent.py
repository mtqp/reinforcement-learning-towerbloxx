from Agent import *

class QAgent(Agent):
    def __init__(self, environment, episodes):
        super(QAgent, self).__init__(environment, episodes)
        self.q_matrix = {}
        self.alpha = 0.5
        self.gamma = 0.8
        self.epsilon = 0.1

        self.th = 0

    def max_action(self, state):
        throw_val = self.q_value((state, Environment.THROW))
        pass_val = self.q_value((state, Environment.PASS))
        if throw_val > pass_val:
            return Environment.THROW
        else:
            return Environment.PASS

    def run_episode(self, to_print):
        state = self.environment.start()
        while not (state.has_finished()):
            action = self.choose_action(state) #usando una politica derivada de Q (eps-greedy en este caso)
            new_state, reward = self.environment.make_action(action)

            max_action = self.max_action(new_state)

            new_value = (1-self.alpha)*self.q_value((state,action)) + self.alpha*(reward + self.gamma*self.q_value((new_state, max_action)))
            self.set_q_value((state, action), new_value)

            state = new_state


            if to_print:
                if reward == 500:
                    self.th += 1
                tower_pos, tower_vel, crane_pos, crane_dir = state.state_factors()
                print crane_pos, tower_pos, self.th, 0, action, reward
                