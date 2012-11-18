# -*- coding: utf-8 *-*

import matplotlib.pyplot as plt


"""
Cómo graficar: (sacado de http://matplotlib.org/users/pyplot_tutorial.html)

1) Grafico simple:
    - plt.plot(y_values)
    - plt.plot(xvalues, yvalues)  # Debe valer que: len(xvalues)==len(yvalues)

2) Muchos graficos en una figura:
    - Subplots:
        plt.figure(1)
        # El primer numero es la cantidad de filas, el segundo es la cant de
        # columnas y el tercero el numero del subgrafico, contando de izquierda
        # a derecha y de arriba hacia abajo
        plt.subplot(211)
        plt.plot(x, y)
        plt.subplot(212)
        plt.plot(x2, y2)
    - Varias funciones en el mismo grafico:
        plt.plot(x1, y1, x2, y2, x3, y3, ...)

"""


def progreso_refuerzos_subplots(refs_q, refs_s):
    plt.subplot(211)
    plt.plot(refs_q)
    plt.title("Progreso de refuerzos para Q Learning")
    plt.xlabel("Nro de episodio")
    plt.ylabel("Suma de los refuerzos por episodio")
    plt.subplot(212)
    plt.plot(refs_s)
    plt.title("Progreso de refuerzos para Sarsa lambda")
    plt.xlabel("Nro de episodio")
    plt.ylabel("Suma de los refuerzos por episodio")
    plt.savefig("progreso_refuerzos_subplots.jpg")

