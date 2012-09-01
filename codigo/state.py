#coding=utf-8

class State(object):

    def __init__(self, environment):
        self._environment = environment
    
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
        return self._environment._finished
    
    def state_factors(self):
        return self._environment.visible_factors()
