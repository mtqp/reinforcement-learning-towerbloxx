from QLambdaAgent import *

class QAgent(QLambdaAgent):
    def __init__(self, environment):
        super(QAgent, self).__init__(environment,1)