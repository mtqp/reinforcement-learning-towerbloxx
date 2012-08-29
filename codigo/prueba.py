from environment import Environment
from Agents.QAgent import QAgent


env = Environment()
sarsa = QAgent(env)
sarsa.learn()
sarsa.what_did_i_learned()


