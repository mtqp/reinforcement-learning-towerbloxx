#coding=utf-8

from environment import Environment
from Agents.QAgent import QAgent
from Agents.SarsaLambda import SarsaLambda


from utils import *
from numpy import average
import time


def qAgent(pisos, desde, alpha, gamma, epsilon):
    env = Environment(tower_height=desde, max_height=desde + pisos)
    return QAgent(env, alpha=alpha, gamma=gamma, epsilon=epsilon)


def sAgent(pisos, desde, alpha, gamma, epsilon, lambda_val=0.3):
    env = Environment(tower_height=desde, max_height=desde + pisos)
    return SarsaLambda(env, alpha=alpha, gamma=gamma, epsilon=epsilon,
                       lambda_val=lambda_val)


def run_for(title, n, agents, formatt, labels):
    data = []

    for j in range(len(agents)):
        start = time.time()
        refs = []
        proms = []
        for i in range(n):
            refs.append(agents[j].run_episode())
            proms.append(average(refs))
        data.append((refs[:], formatt[j], labels[j]))
        data.append((proms[:], formatt[j][0] + '-', 'Promedio'))
        elapsed = time.time() - start

        print "Time taken for", labels[j], ": ", elapsed, "seconds."

    plot_all(title, data)


def comparacion_epsilon_q(n):

    qagent1 = qAgent(pisos=20, desde=20, alpha=0.7, gamma=0.8, epsilon=0)
    qagent2 = qAgent(pisos=20, desde=20, alpha=0.7, gamma=0.8, epsilon=0.0001)
    qagent3 = qAgent(pisos=20, desde=20, alpha=0.7, gamma=0.8, epsilon=0.001)
    qagent4 = qAgent(pisos=20, desde=20, alpha=0.7, gamma=0.8, epsilon=0.01)

    run_for(
        u"Comparación Epsilons en QLearning",
        n,
        [qagent1, qagent2, qagent3, qagent4],
        ["y.", "m.", "c.", "r."],
        ["Q(e=0)", "Q(e=0.0001)", "Q(e=0.001)", "Q(e=0.01)"]
    )


def comparacion_epsilon_sarsa(n):

    sagent1 = sAgent(pisos=20, desde=20, alpha=0.7, gamma=0.8, epsilon=0)
    sagent2 = sAgent(pisos=20, desde=20, alpha=0.7, gamma=0.8, epsilon=0.0001)
    sagent3 = sAgent(pisos=20, desde=20, alpha=0.7, gamma=0.8, epsilon=0.001)
    sagent4 = sAgent(pisos=20, desde=20, alpha=0.7, gamma=0.8, epsilon=0.01)

    run_for(
        u"Comparación Epsilons en Sarsa-Lambda",
        n,
        [sagent1, sagent2, sagent3, sagent4],
        ["y.", "m.", "c.", "r."],
        ["Sarsa(e=0)", "Sarsa(e=0.0001)", "Sarsa(e=0.001)", "Sarsa(e=0.01)"]
    )


def comparacion_gamma(n):
    qagent1 = qAgent(pisos=20, desde=20, alpha=0.7, gamma=0.2, epsilon=0.001)
    qagent2 = qAgent(pisos=20, desde=20, alpha=0.7, gamma=0.5, epsilon=0.001)
    qagent3 = qAgent(pisos=20, desde=20, alpha=0.7, gamma=0.8, epsilon=0.001)

    run_for(
        u"Comparación Gammas en QLearning",
        n,
        [qagent1, qagent2, qagent3],
        ["g.", "r.", "b."],
        ["QAgent gamma=0.2", "QAgent gamma=0.5", "QAgent gamma=0.8"]
    )


def comparacion_alpha(n):
    qagent0 = qAgent(pisos=20, desde=20, alpha=0, gamma=0.7, epsilon=0.001)
    qagent1 = qAgent(pisos=20, desde=20, alpha=0.2, gamma=0.7, epsilon=0.001)
    qagent2 = qAgent(pisos=20, desde=20, alpha=0.5, gamma=0.7, epsilon=0.001)
    qagent3 = qAgent(pisos=20, desde=20, alpha=0.8, gamma=0.7, epsilon=0.001)

    run_for(
        u"Comparación Alphas en QLearning",
        n,
        [qagent0, qagent1, qagent2, qagent3],
        ["m.", "c.", "r.", "b."],
        ["", "QAgent alpha=0.2", "QAgent alpha=0.5", "QAgent alpha=0.8"]
    )


def comparacion_qlearning_vs_sarsa(n):
    qagent = qAgent(pisos=20, desde=20, alpha=0.7, gamma=0.8, epsilon=0.001)
    sarsa = sAgent(pisos=20, desde=20, alpha=0.7, gamma=0.8, lambda_val = 0.001, epsilon=0.001)
    sarsa2 = sAgent(pisos=20, desde=20, alpha=0.7, gamma=0.8, lambda_val = 0.3, epsilon=0.001)
    sarsa3 = sAgent(pisos=20, desde=20, alpha=0.7, gamma=0.8, lambda_val = 0.7, epsilon=0.001)

    run_for(
        u"Comparación QLearning vs Sarsas",
        n,
        [qagent, sarsa, sarsa2, sarsa3],
        ["c.", "m.", "r.", "b."],
        ["QLearning", "Sarsa (lamda=0.001)", "Sarsa (lamda=0.03)", "Sarsa (lambda=0.07)"]
    )


comparacion_qlearning_vs_sarsa(200)
