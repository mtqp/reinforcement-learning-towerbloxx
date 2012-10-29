
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from environment import Environment
from Agents.SarsaLambda import SarsaLambda
from Agents.QAgent import QAgent

env = Environment()
agent = QAgent(env)
#agent = SarsaLambda(0.2,env)

data = [0 for i in range(300)]
fig = plt.figure()
ax = fig.add_subplot(111)

line, = ax.plot(np.array(data),'g.')

ax.set_ylim(-10000, 10000)

def update(data):
    line.set_ydata(data)
    return line

def data_gen():
    totalRefuerzos = 0
    movimientos = 0
    global data
    global agent
    global env
    max_ref = 0
    while True:
      data = data[1:]
      ref = agent.run_episode()
      totalRefuerzos += ref
      if ref > max_ref:
        max_ref = ref
      movimientos += 1
      print str(movimientos) + ": " + str(ref) + " prom:" + str(totalRefuerzos/float(movimientos)) + " Max: " + str(max_ref) + " #states: " + str(env.states_action_pair_count)
      data.append(ref)
      yield np.array(data)

ani = animation.FuncAnimation(fig, update, data_gen, interval=1)
plt.show()
