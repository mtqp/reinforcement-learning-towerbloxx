
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from environment import Environment
from Agents.SarsaLambda import SarsaLambda
from Agents.QAgent import QAgent

env = Environment()
agent = QAgent(env)
#agent = SarsaLambda(0.2,env)

data = [0 for i in range(100)]
data2 = [0 for i in range(100)]
fig = plt.figure()
ax = fig.add_subplot(111)

line, = ax.plot(np.array(data))
line2, = ax.plot(np.array(data2))

ax.set_ylim(-100, 100)

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
      data2 = data2[1:]
      ref = agent.run_episode()
      totalRefuerzos += ref
      if ref > max_ref:
        max_ref = ref
      movimientos += 1
      print str(movimientos) + ": " + str(ref) + " prom:" + str(totalRefuerzos/float(movimientos)) + " Max: " + str(max_ref)
      data2.append(max_ref)
      data.append(ref)
      yield np.array(data)

ani = animation.FuncAnimation(fig, update, data_gen, interval=1)
plt.show()
