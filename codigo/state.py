
class State:
    def __init__(self, environment):
        self.environment = environment
        self._finish = None

    def finish(self):
        self._finish = True

    def has_finished(self):
        return self._finish

    def state_factors(self):
        return self.environment.visible_factors()
