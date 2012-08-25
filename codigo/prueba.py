from environment import Environment
from Agents.QAgent import QAgent
from Agents.RMax import RMax


env = Environment()
qa = QAgent(env)
print "QAgent learing..."
qa.learn()
print "QAgent learned"
rmax = RMax(env)
print "RMax learing..."
rmax.learn()
print "RMax learned"