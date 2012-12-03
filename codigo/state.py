#coding=utf-8
class State(object):
    def __init__(self, environment):
        self.environment = environment


    def __str__(self):
        return str(self.environment)
    
    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(self.state_factors())

    def has_finished(self):
        return self.environment._finished
    
    def state_factors(self):
        str(self)

    