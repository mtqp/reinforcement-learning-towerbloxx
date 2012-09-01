from Agent import *

class SarsaLambda(Agent):
    #Siguiendo el algoritmo del libro de Sutton & Barto
    def __init__(self, environment, lambda_val):
        super(SarsaLambda, self).__init__(environment)
        self.q_matrix = {}
        self.alpha = 0.5
        self.gamma = 0.8
        self.epsilon = 0.9
        self.elegibilities = {}
        self.lambda_val = lambda_val

    def run_episode(self):
        state = self.environment.start()
        action = Environment.PASS #inicializacion de la action (random)
        sum_of_rewards = 0 #TODO: Eliminar
        
        while not (state.has_finished()):
            new_state, reward = self.environment.make_action(action)
            new_action = self.choose_action(new_state) #usando una politica derivada de Q (eps-greedy en este caso)
            delta = reward + self.gamma * self.q_value((new_state, new_action)) - self.q_value((state, action))

            self.elegibilities[(state,action)] = self.e_value((state, action)) + 1 

            for key in self.elegibilities.keys(): #ACA INVENTE! hay que chquear que este bien esta recorrida.. se supone que es para todo s,a
                self.q_matrix[key] = self.q_value(key) + self.alpha * delta * self.e_value(key)
                self.elegibilities[key] = self.gamma * self.lambda_val * self.e_value(key)

            state = new_state
            action = new_action

            sum_of_rewards += reward

       
        if sum_of_rewards > self.maxs:
            self.maxs = sum_of_rewards
            #Info para debug: #TODO: Eliminar
            print "Reward del episodio: " + str(sum_of_rewards)


