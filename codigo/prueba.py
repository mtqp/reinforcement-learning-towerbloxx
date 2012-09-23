from environment import Environment
from Agents.SarsaLambdaAgent import SarsaLambda
from Agents.QAgent import QAgent
from Agents.RMax import RMax
env = Environment()
agent = RMax(env)
agent.learn()
