from environment import Environment
from Agents.QAgent import QAgent
from Agents.SarsaLambda import SarsaLambda

def qAgent(pisos, desde, alpha, gamma, epsilon):
  env = Environment(tower_height = desde, max_height = desde + pisos)
  return QAgent(env, alpha = alpha, gamma = gamma, epsilon = epsilon)


totalRefuerzos = 0
movimientos = 0

#agent = sAgent(pisos = 10, desde = 10, alpha = 0.4, gamma = 0.6, epsilon = 0.001, lambda_val = 0.4)

agent = qAgent(pisos = 10, desde = 10, alpha = 0.4, gamma = 0.6, epsilon = 0.001)

while True:
  ref = agent.run_episode()
  totalRefuerzos += ref
  movimientos += 1
  print str(movimientos) + ": " + str(ref) + " prom:" + str(totalRefuerzos/float(movimientos))

