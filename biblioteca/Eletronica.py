import numpy as np

def Serie(resistores):
    """ Serie de resistores """
    return(np.sum(resistores))
def Paralelo(resistores):
    """ Paralelo de resistores """
    resistores = np.array(resistores)
    return(1/np.sum(1/resistores))

def Malha(R,V):
    return np.linalg.solve(R,V)