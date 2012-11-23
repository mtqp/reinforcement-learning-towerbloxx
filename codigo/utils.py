# -*- coding: utf-8 *-*

import matplotlib.pyplot as plt

def plot_all(title, graphs):
    plots = []
    legends = []
    plt.figure()
    for data, color, legend in graphs:
        p, = plt.plot(data, color)
        plots.append(p)
        legends.append(legend)
    plt.title(title)
    plt.xlabel("Episodios")
    plt.ylabel("Refuerzo")
    plt.legend(plots, legends, loc = 4,prop={'size':6}) #4 es abajo a la derecha
   
    plt.savefig(title+".svg")
    
    
