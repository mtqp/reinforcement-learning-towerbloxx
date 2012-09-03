from Agent import *

class QAgent(Agent):
    def __init__(self, environment):
        super(QAgent, self).__init__(environment)
        self.q_matrix = {}
        self.alpha = 0.5
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
        sum_of_rewards = 0 #TODO: Eliminar
        steps = 0
        while not (state.has_finished()):
            steps += 1
            action = self.choose_action(state) #usando una politica derivada de Q (eps-greedy en este caso)
            new_state, reward = self.environment.make_action(action)
#            print new_state.state_factors(), " TIRO" if action else " PASO"

            max_action = self.max_action(new_state)

            self.q_matrix[(state, action)] = (1-self.alpha)*self.q_value((state,action)) + self.alpha*(reward + self.gamma*self.q_value((new_state, max_action)))

            state = new_state
            sum_of_rewards += reward


        print sum_of_rewards, steps, (new_state.environment.tower_height - 10)
