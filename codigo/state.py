class State(object):
    _instances = {}
    def __new__(cls, state):
        if not cls._instances.get(state, None):
            cls._instances[state] = super(State, cls).__new__(cls, state)
        return cls._instances[state]


    def __init__(self, state):
        self._finish = None
        self._state = state

    def finish(self):
        self._finish = True

    def has_finished(self):
        return self._finish

    def state_factors(self):
        return self._state
