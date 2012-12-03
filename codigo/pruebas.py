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
            print i
            refs.append(agents[j].run_episode())
            proms.append(average(refs))
        data.append((refs[:], formatt[j], labels[j]))
        data.append((proms[:], formatt[j][0] + '-', 'Promedio'))
        elapsed = time.time() - start

        print "Time taken for", labels[j], ": ", elapsed, "seconds."

    plot_all(title, data)


def comparacion_epsilon_q(n):

    qagent1 = qAgent(pisos=10, desde=50, alpha=0.7, gamma=0.8, epsilon=0)
    qagent2 = qAgent(pisos=10, desde=50, alpha=0.7, gamma=0.8, epsilon=0.0001)
    qagent3 = qAgent(pisos=10, desde=50, alpha=0.7, gamma=0.8, epsilon=0.001)
    qagent4 = qAgent(pisos=10, desde=50, alpha=0.7, gamma=0.8, epsilon=0.01)

    run_for(
        u"Comparación Epsilons en QLearning",
        n,
        [qagent1, qagent2, qagent3, qagent4],
        ["y.", "m.", "c.", "r."],
        ["Q(e=0)", "Q(e=0.0001)", "Q(e=0.001)", "Q(e=0.01)"]
    )


def comparacion_epsilon_sarsa(n):

    sagent1 = sAgent(pisos=10, desde=50, alpha=0.7, gamma=0.8, epsilon=0)
    sagent2 = sAgent(pisos=10, desde=50, alpha=0.7, gamma=0.8, epsilon=0.0001)
    sagent3 = sAgent(pisos=10, desde=50, alpha=0.7, gamma=0.8, epsilon=0.001)
    sagent4 = sAgent(pisos=10, desde=50, alpha=0.7, gamma=0.8, epsilon=0.01)

    run_for(
        u"Comparación Epsilons en Sarsa-Lambda ",
        n,
        [sagent1, sagent2, sagent3, sagent4],
        ["y.", "m.", "c.", "r."],
        ["Sarsa(e=0)", "Sarsa(e=0.0001)", "Sarsa(e=0.001)", "Sarsa(e=0.01)"]
    )


def comparacion_gamma(n):
    qagent1 = qAgent(pisos=10, desde=50, alpha=0.7, gamma=0.2, epsilon=0.001)
    qagent2 = qAgent(pisos=10, desde=50, alpha=0.7, gamma=0.5, epsilon=0.001)
    qagent3 = qAgent(pisos=10, desde=50, alpha=0.7, gamma=0.8, epsilon=0.001)

    run_for(
        u"Comparación Gammas en QLearning",
        n,
        [qagent1, qagent2, qagent3],
        ["g.", "r.", "b."],
        ["QAgent gamma=0.2", "QAgent gamma=0.5", "QAgent gamma=0.8"]
    )


def comparacion_alpha(n):
    qagent0 = qAgent(pisos=10, desde=50, alpha=0.0, gamma=0.7, epsilon=0.001)
    qagent1 = qAgent(pisos=10, desde=50, alpha=0.2, gamma=0.7, epsilon=0.001)
    qagent2 = qAgent(pisos=10, desde=50, alpha=0.5, gamma=0.7, epsilon=0.001)
    qagent3 = qAgent(pisos=10, desde=50, alpha=0.8, gamma=0.7, epsilon=0.001)
    qagent4 = qAgent(pisos=10, desde=50, alpha=1.0, gamma=0.7, epsilon=0.001)

    run_for(
        u"Comparación Alphas en QLearning",
        n,
        [qagent0, qagent1, qagent2, qagent3, qagent4],
        ["m.", "c.", "r.", "b.","k."],
        ["QAgent alpha=0", "QAgent alpha=0.2", "QAgent alpha=0.5", "QAgent alpha=0.8","QAgent alpha=1"]
    )


def comparacion_qlearning_vs_sarsa(n):
    qagent = qAgent(pisos=10, desde=50, alpha=0.7, gamma=0.8, epsilon=0.001)
    sarsa = sAgent(pisos=10, desde=50, alpha=0.7, gamma=0.8, lambda_val = 0.001, epsilon=0.001)
    sarsa2 = sAgent(pisos=10, desde=50, alpha=0.7, gamma=0.8, lambda_val = 0.3, epsilon=0.001)
    sarsa3 = sAgent(pisos=10, desde=50, alpha=0.7, gamma=0.8, lambda_val = 0.7, epsilon=0.001)

    run_for(
        u"Comparación QLearning vs Sarsas",
        n,
        [qagent, sarsa, sarsa2, sarsa3],
        ["c.", "m.", "r.", "b."],
        ["QLearning", "Sarsa (lamda=0.001)", "Sarsa (lamda=0.03)", "Sarsa (lambda=0.07)"]
    )


def q_learning_problema_inestable(n):

    qagent1 = qAgent(pisos=10, desde=70, alpha=0.7, gamma=0.8, epsilon=0.01)
    qagent2 = qAgent(pisos=10, desde=50, alpha=0.7, gamma=0.8, epsilon=0.01)
    qagent3 = qAgent(pisos=10, desde=30, alpha=0.7, gamma=0.8, epsilon=0.01)
    qagent4 = qAgent(pisos=10, desde=20, alpha=0.7, gamma=0.8, epsilon=0.01)
    qagent5 = qAgent(pisos=10, desde=10, alpha=0.7, gamma=0.8, epsilon=0.01)
    qagent6 = qAgent(pisos=10, desde=1, alpha=0.7, gamma=0.8, epsilon=0.01)

    run_for(
        u"Comparación QLearning con distintas estabilidades",
        n,
        [qagent1, qagent2, qagent3, qagent4,qagent5,qagent6],
        ["y.", "c.", "m.", "r.","g.","b."],
        ["Q70","Q50","Q30","Q20","Q10","Q1"]
    )

def sarsa_lambda_problema_inestable(n):

    sagent1 = sAgent(pisos=10, desde=70, alpha=0.7, gamma=0.8, epsilon=0.01)
    sagent2 = sAgent(pisos=10, desde=50, alpha=0.7, gamma=0.8, epsilon=0.01)
    sagent3 = sAgent(pisos=10, desde=30, alpha=0.7, gamma=0.8, epsilon=0.01)
    sagent4 = sAgent(pisos=10, desde=20, alpha=0.7, gamma=0.8, epsilon=0.01)
    sagent5 = sAgent(pisos=10, desde=10, alpha=0.7, gamma=0.8, epsilon=0.01)
    sagent6 = sAgent(pisos=10, desde=1, alpha=0.7, gamma=0.8, epsilon=0.01)

    run_for(
        u"Comparación Sarsa con distintas estabilidades",
        n,
        [sagent1, sagent2, sagent3, sagent4,sagent5,sagent6],
        ["y.", "c.", "m.", "r.","g.","b."],
        ["S70","S50","S30","S20","S10","S1"]
    )



#comparacion_epsilon_q(3000)
#comparacion_alpha(4000)
#comparacion_gamma(3000)
q_learning_problema_inestable(3000)
#comparacion_qlearning_vs_sarsa(3000)
#sarsa_lambda_problema_inestable(1000)