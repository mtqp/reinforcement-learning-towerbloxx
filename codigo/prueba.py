from environment import Environment
from Agents.QAgent import QAgent
from Agents.QLambdaAgent import QLambdaAgent


env = Environment()
qlambda = QAgent(env)
qlambda.learn()
qlambda.what_did_i_learned()


