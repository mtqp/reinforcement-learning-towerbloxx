from Agent import *

class QLambdaAgent(Agent):
    MAX_TRIES = 100
    #Siguiendo el algoritmo de: http://tinyurl.com/c3n75nx
    def __init__(self, environment, lambda_val):
        super(QLambdaAgent, self).__init__(environment)
        self.q_matrix = {}
        self.alpha = 0.5
        self.gamma = 0.9
        self.epsilon = 0.3
        self.elegibilities = {}
        self.lambda_val = lambda_val

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
        action = Environment.PASS #inicializacion de la action (random)
        tries = 0
        

        sum_of_rewards = 0 #TODO: Eliminar
        
        while not (state.has_finished() or tries == self.MAX_TRIES):
            tries += 1
            new_state, reward = self.environment.make_action(action)
            new_action = self.choose_action(new_state) #usando una politica derivada de Q (eps-greedy en este caso)

            best_action = self.max_action(new_state)
            delta = reward + self.gamma * self.q_value((new_state, best_action)) - self.q_value((state, action))

            self.elegibilities[(state,action)] = self.e_value((state, action)) + 1 

            for key in self.elegibilities.keys(): #ACA INVENTE! hay que chquear que este bien esta recorrida.. se supone que es para todo s,a
                self.q_matrix[key] = self.q_value(key) + self.alpha * delta * self.e_value(key)
                if new_action == best_action:
                    self.elegibilities[key] = self.gamma * self.lambda_val * self.e_value(key)
                else:
                    self.elegibilities[key] = 0

            state = new_state
            action = new_action

            sum_of_rewards += reward

       
        #Info para debug: #TODO: Eliminar
        print "Reward promedio: " + str(sum_of_rewards / tries)
        if tries == self.MAX_TRIES:
            print "Max tries!!"

        print "-----------------------------------END OF EPISODE------------------------------------------"

    def max_action(self, state):
        throw_val = self.q_value((state, Environment.THROW))
        pass_val = self.q_value((state, Environment.PASS))
        return max(throw_val, pass_val)
    
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

