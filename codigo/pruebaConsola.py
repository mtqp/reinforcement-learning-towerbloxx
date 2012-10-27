from environment import Environment
from Agents.SarsaLambda import SarsaLambda

totalRefuerzos = 0
movimientos = 0

env = Environment()
agent = SarsaLambda(0.1,env)
while True:
  ref = agent.run_episode()
  totalRefuerzos += ref
  movimientos += 1
  print str(movimientos) + ": " + str(ref) + " prom:" + str(totalRefuerzos/float(movimientos))