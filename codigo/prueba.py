from environment import Environment
from Agents.SarsaLambdaAgent import SarsaLambda
from Agents.QAgent import QAgent

env = Environment()
agent = QAgent(env, 10000)
agent.learn()
agent.what_did_i_learned()