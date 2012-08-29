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

    
    def q_value(self, key):
        return self.q_matrix.get(key, 0)

    def e_value(self,key):
        return self.elegibilities.get(key,0)
    
    def learn(self):
        for i in range(1000):
            self.run_episode()
            print "Episodio numero: " + str(i) #TODO: Elminar

    def run_episode(self):
        state = self.environment.start()
        sum_of_rewards = 0 #TODO: Eliminar
        
        while not (state.has_finished()):
            print state.state_factors()
            action = self.choose_action(state) #usando una politica derivada de Q (eps-greedy en este caso)
            new_state, reward = self.environment.make_action(action)

            max_action = self.max_action(new_state)

            self.q_matrix[(state, action)] = (1-self.alpha)*self.q_value((state,action)) + self.alpha*(reward + self.gamma*self.q_value((new_state, max_action)))

            state = new_state
            sum_of_rewards += reward

       
        #Info para debug: #TODO: Eliminar
        print "Reward del episodio: " + str(sum_of_rewards)
        print "-----------------------------------END OF EPISODE------------------------------------------"


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
        print "#of States: " + str(len(self.q_matrix.keys()))

