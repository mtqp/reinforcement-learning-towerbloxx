from environment import Environment
from Agents.SarsaLambdaAgent import SarsaLambda


env = Environment()
sarsa = SarsaLambda(env, 0.1)
sarsa.learn()
sarsa.what_did_i_learned()


