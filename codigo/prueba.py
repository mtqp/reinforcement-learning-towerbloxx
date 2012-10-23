from environment import Environment
from Agents.SarsaLambda import SarsaLambda
from Agents.QAgent import QAgent
from Agents.RMax import RMax
env = Environment()
agent = SarsaLambda(0.8,env)
agent.learn()
