#coding=utf-8

import math

def alejar_de_cero(f):
    if f<0:
        return math.floor(f)
    else:
        return math.ceil(f)


class State(object):

    def __init__(self, environment):
        self.environment = environment
    
    def __eq__(self, obj):
        return self.state_factors() == obj.state_factors()
    
    def __hash__(self):
        """
        Se tiene que definir para que se pueda usar como clave en un diccionario
        o para usarse dentro de un conjunto. Además, si no están definidas las
        comparaciones, sirve para decidir si 2 estados son iguales.
        """
        factors = self.state_factors()
        return factors.__hash__()

    def has_finished(self):
        return self.environment._finished
    
    def state_factors(self):
        factors = self.discretized_factors()
        return factors

    def discretized_factors(self):
        tower_pos = self.environment.tower_pos
        tower_vel = self.environment.tower_vel
        crane_pos = self.environment.crane_pos
        crane_dir = self.environment.crane_direction
        return tower_pos, tower_vel, crane_pos, crane_dir