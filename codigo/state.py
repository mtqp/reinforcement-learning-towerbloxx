class State(object):
    _instances = {}
    _misses = 0

    def __new__(cls, environment):
        factors = environment.visible_factors()

        if not cls._instances.get(factors, None):
            print str(factors) + " (" + str(len(cls._instances.keys())) +  " of: " + str(99*2*99*10) + " states)"
            cls._instances[factors] = super(State, cls).__new__(cls, environment)
        return cls._instances[factors]


    def __init__(self, environment):
        self._environment = environment

    def has_finished(self):
        return self._environment._finished
    
    def state_factors(self):
        return self._environment.visible_factors()
