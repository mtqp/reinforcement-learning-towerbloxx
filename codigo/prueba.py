from environment import Environment
from Agents.QAgent import QAgent
from Agents.QLambdaAgent import QLambdaAgent


env = Environment()
qa = QAgent(env)
print "QAgent learing..."
qa.learn()
print "QAgent learned"

qlambda = QLambdaAgent(env,4)
print "QLambdaAgent(4) learing..."
qlambda.learn()
print "QLambdaAgent(4) learned"