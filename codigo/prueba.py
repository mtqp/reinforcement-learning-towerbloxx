

from environment import Environment
from agent import QAgent

env = Environment()
qa = QAgent(env)

qa.learn()