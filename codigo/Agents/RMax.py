
from copy import deepcopy
import random
from Agent import *

RMAX_GAMMA_VALUE_ITER = 0.85
RMAX_EPSILON_VALUE_ITER = 1
RMAX = 300
class RMax(object):
  def __init__(self,environment):
    self.learned_rewards = {} #el acumulado, no el valor real
    self.learned_transitions = {} #la cantidad de veces que nos movimos
    self.learned_count = {} #dado un par (accion, estado), la cantidad de veces que hicimos la accion partiendo del estado
    self.visited_states = set([])
    self.vmax = RMAX / (1 - RMAX_GAMMA_VALUE_ITER)
    self.reachable_states = set([])
    self.values = {}
    self.environment = environment
      
  def learn(self):
    for i in range(1):
      self.run_episode()
  
  def run_episode(self):
    state = self.environment.start()
    while not (state.has_finished()):
      action = self.choose_action(state)
      new_state, reward = self.environment.make_action(action)
      self.update_model(state, action, reward, new_state)
      state = deepcopy(new_state)

  def update_model(self, state, action, reward, next_state):
    self.increase_count(action, state) #actualizo cantidad de veces que hicimos de estado a accion
    self.update_R_value(action, state, reward) #actualizo reward
    self.increase_T_value(action, state, next_state) #actualizo chance de nuevo estado dado accion estado
    #actualizo visitados (blancos)
    self.visited_states.add(state)
    #actualizo alcanzables (blancos o grises)
    self.reachable_states.add(state)
    #actualizo alcanzables (blancos o grises)
    if not next_state.has_finished(): 
      self.reachable_states.add(next_state)
    
  def choose_action(self, state):
    print state
    values = self.values
    Q = {} #los q estimados
    continue_iter = True #si seguimos iterando
    while continue_iter:
      for visited in self.visited_states:
        for action in [0,1]: #actions
          partial_Q = self.R_value(action, visited) #inicializo con el reward dado el estado y la accion
          for possible in self.reachable_states: #todos los estados que se que existen
            if values.get(possible) is None:
              value_to_use = 0.0 if possible in self.visited_states else self.vmax #si no esta, uso vmax
            else:
              previous, current = values.get(possible) #si esta, uso el previous
              value_to_use = previous #da lo mismo cual usar entre previous y current, a esta altura son lo mismo
              #a continuacion, cambio current para comparar con el error, pero, al final de la iteracion
              #seteo el previous con el current
            partial_Q += RMAX_GAMMA_VALUE_ITER * self.T_value(action, visited, possible) * value_to_use
            #pongo el valor anterior si es aproximable, o vmax si no es aproximable (si nunca voy a saber nada)
            #todo multiplicado por el gamma, obvio
          Q[(action,visited)] = partial_Q
        previous, current = values.get(visited) or (0.0,0.0)
        values[visited] = previous, max([Q[(a,visited)] for a in [0,1]]) #el valor es el maximo de los Q
        #actualizo el current con el maximo de los Q, o sea, el V obtenido
      
      differences = [abs((i-j)) for(i,j) in values.values()]
      err = max(differences) if differences != [] else 0 #norma infinito, norma 2 tiraba overflow
      continue_iter = err > RMAX_EPSILON_VALUE_ITER #si es mayor al epsilon, sigo iterando. si no, no.
      for (key, value) in values.iteritems():
        previous, current = value
        values[key] = (current, current) # el previous lo seteo en el current
    
    #bien, ya sali
    #ahora, dado el Q, quiero la accion que maximice
    qMax = max([(Q.get((a,state)) or 0.0) for a in [0,1]])
    if (Q.get((a,state))or 0.0) == qMax:
      return 1
    else:
      return 0

  def R_value(self, action, state): #dado un estado y una accion, su reward empirico, o rmax si alguno no conocido
    reward = self.learned_rewards.get((action,state))
    count = self.learned_count.get((action,state))
    if reward is None:
      return RMAX
    else:
      return reward/float(count)
    
  def update_R_value(self, action, state, reward): #se updatea el reward dado un estado y la accion
    prev_reward = self.learned_rewards.get((action,state)) or 0.0
    self.learned_rewards[(action,state)] = reward + prev_reward
  
  def T_value(self, action, state, next_state): #dado un estado, la accion y el siguiente estado, devuelve la probabilidad de moverse
    movements = self.learned_transitions.get((action,state,next_state))
    count = self.learned_count.get((action,state))
    if movements is None:
      return 0.0
    else:
      return float(movements)/float(count)
      
  def increase_T_value(self, action, state, next_state):
    prev_value = self.learned_transitions.get((action,state,next_state)) or 0
    self.learned_transitions[(action,state,next_state)] = prev_value + 1
      
  def increase_count(self, action, state):
    count = self.learned_count.get((action,state)) or 0
    self.learned_count[(action, state)] = count + 1
    
