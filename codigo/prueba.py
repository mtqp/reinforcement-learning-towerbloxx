from environment import Environment
from Agents.QAgent import QAgent
from Agents.QLambdaAgent import QLambdaAgent


env = Environment()
qlambda = QLambdaAgent(env,2)
print "QLambdaAgent(4) learing..."
qlambda.learn()
print "QLambdaAgent(4) learned:"

qlambda.what_did_i_learned()


