from environment import Environment
from Agents.QAgent import QAgent
from Agents.SarsaLambda import SarsaLambda


from utils import *
from numpy import average


def qAgent(pisos, desde, alpha, gamma, epsilon):
    env = Environment(tower_height=desde, max_height=desde + pisos)
    return QAgent(env, alpha=alpha, gamma=gamma, epsilon=epsilon)


def sAgent(pisos, desde, alpha, gamma, epsilon, lambda_val=0.3):
    env = Environment(tower_height=desde, max_height=desde + pisos)
    return SarsaLambda(env, alpha=alpha, gamma=gamma, epsilon=epsilon,
                       lambda_val=lambda_val)



def progreso_de_refuerzos():
    #sagent = sAgent(pisos=4, desde=40, alpha=0.7, gamma=0.8, epsilon=0.01)
    qagent = qAgent(pisos=20, desde=20, alpha=0.4, gamma=0.7, epsilon=0.01)
    sagent = qAgent(pisos=20, desde=20, alpha=0.7, gamma=0.8, epsilon=0.01)
    ref_q, ref_s, prom_q, prom_s = [], [], [], []
    
    for i in range(1000):
        ref_q.append(qagent.run_episode())
        ref_s.append(sagent.run_episode())
        prom_q.append(average(ref_q))
        prom_s.append(average(ref_s))

    progreso_refuerzos_plot(ref_q, ref_s, prom_q, prom_s)



progreso_de_refuerzos()






