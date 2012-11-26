
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from environment import Environment
from Agents.QAgent import QAgent
from Agents.SarsaLambda import SarsaLambda

def qAgent(pisos, desde, alpha, gamma, epsilon):
  env = Environment(tower_height = desde, max_height = desde + pisos)
  return QAgent(env, alpha = alpha, gamma = gamma, epsilon = epsilon)

def sAgent(pisos, desde, alpha, gamma, epsilon, lambda_val = 0.3):
  env = Environment(tower_height = desde, max_height = desde + pisos)
  return SarsaLambda(env, alpha = alpha, gamma = gamma, epsilon = epsilon, lambda_val = lambda_val)


agent = qAgent(pisos = 10, desde = 50, alpha = 0.7, gamma = 0.8, epsilon = 0.1)

data = [0 for i in range(300)]
fig = plt.figure()
ax = fig.add_subplot(111)

line, = ax.plot(np.array(data),'g.')

ax.set_ylim(-15000, 15000)

def update(data):
    line.set_ydata(data)
    return line

def data_gen():
    totalRefuerzos = 0
    movimientos = 0
    global data
    global agent
    max_ref = 0
    while True:
      data = data[1:]
      ref = agent.run_episode()
      totalRefuerzos += ref
      if ref > max_ref:
        max_ref = ref
      movimientos += 1
      data.append(ref)
      yield np.array(data)

ani = animation.FuncAnimation(fig, update, data_gen, interval=1)
plt.show()
