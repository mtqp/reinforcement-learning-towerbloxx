from environment import Environment
from Agents.QAgent import QAgent
from Agents.SarsaLambda import SarsaLambda
from utils import progreso_refuerzos_subplots

def qAgent(pisos, desde, alpha, gamma, epsilon):
    env = Environment(tower_height=desde, max_height=desde + pisos)
    return QAgent(env, alpha=alpha, gamma=gamma, epsilon=epsilon)


def sAgent(pisos, desde, alpha, gamma, epsilon, lambda_val=0.3):
    env = Environment(tower_height=desde, max_height=desde + pisos)
    return SarsaLambda(env, alpha=alpha, gamma=gamma, epsilon=epsilon,
                       lambda_val=lambda_val)



def progreso_de_refuerzos():
    sagent = sAgent(pisos=40, desde=40, alpha=0.7, gamma=0.8, epsilon=0.004)
    qagent = qAgent(pisos=10, desde=10, alpha=0.4, gamma=0.6, epsilon=0.001)
    ref_q, ref_s = [], []
    for i in range(10):
        ref_q.append(qagent.run_episode())
        ref_s.append(sagent.run_episode())

    progreso_refuerzos_subplots(ref_q, ref_s)



#totalRefuerzos = 0
#movimientos = 0

#agent = sAgent(pisos=40, desde=40, alpha=0.7, gamma=0.8, epsilon=0.004)

##agent = qAgent(pisos=10, desde=10, alpha=0.4, gamma=0.6, epsilon=0.001)


#for i in range(10000):
    #ref = agent.run_episode()
    #totalRefuerzos += ref
    #movimientos += 1
    #print str(movimientos) + ": " + str(ref) + " prom:" + str(totalRefuerzos/float(movimientos))



progreso_de_refuerzos()






