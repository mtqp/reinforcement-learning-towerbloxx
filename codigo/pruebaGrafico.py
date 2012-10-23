
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from environment import Environment
from Agents.QAgent import QAgent


env = Environment()
agent = QAgent(env)

data = range(1000)

fig = plt.figure()
ax = fig.add_subplot(111)
line, = ax.plot(np.array(data))
ax.set_ylim(-15000, 15000)

def update(data):
    line.set_ydata(data)
    return line,

def data_gen():
    global data
    global agent
    while True:
      data = data[1:]
      data.append(agent.run_episode())
      yield np.array(data)

ani = animation.FuncAnimation(fig, update, data_gen, interval=100)
plt.show()

#env = Environment()
#agent = SarsaLambda(0.8,env)

#data = []
#data.append(agent.run_episode())

#
#
#for i in range(100):
#  data.append(agent.run_episode())