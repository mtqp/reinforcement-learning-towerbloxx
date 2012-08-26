class State(object):
    _instances = {}

    def __new__(cls, environment):
        factors = environment.visible_factors()
        if not cls._instances.get(factors, None):
            cls._instances[factors] = super(State, cls).__new__(cls, environment)
        return cls._instances[factors]


    def __init__(self, environment):
        self._finish = None
        self._environment = environment

    def finish(self):
        self._finish = True

    def has_finished(self):
        return self._finish

    def state_factors(self):
        return self._environment.visible_factors()
