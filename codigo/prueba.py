from environment import Environment
from Agents.SarsaLambdaAgent import SarsaLambda
from Agents.QAgent import QAgent

env = Environment()
sarsa = SarsaLambda(env,0.8)
sarsa.learn()
sarsa.what_did_i_learned()


