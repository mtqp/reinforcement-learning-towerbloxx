
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from environment import Environment
from Agents.SarsaLambda import SarsaLambda
from Agents.QAgent import QAgent

totalRefuerzos = 0
movimientos = 0

env = Environment()
agent = QAgent(env)
#agent = SarsaLambda(0.2,env)


data = range(100)

fig = plt.figure()
ax = fig.add_subplot(111)
line, = ax.plot(np.array(data), 'g>')
ax.set_ylim(-2000, 2000)

def update(data):
    line.set_ydata(data)
    return line,

def data_gen():
    global data
    global totalRefuerzos
    global movimientos
    global agent
    while True:
      data = data[1:]
      ref = agent.run_episode()
      totalRefuerzos += ref
      movimientos += 1
      print str(movimientos) + ": " + str(ref) + " prom:" + str(totalRefuerzos/float(movimientos))
      data.append(ref)
      yield np.array(data)

ani = animation.FuncAnimation(fig, update, data_gen, interval=1)
plt.show()

#env = Environment()
#agent = SarsaLambda(0.8,env)

#data = []
#data.append(agent.run_episode())

#
#
#for i in range(100):
#  data.append(agent.run_episode())