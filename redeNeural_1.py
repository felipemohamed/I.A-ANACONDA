"""
Created on Thu Jun  4 10:31:30 2020

@author: FelipeMohamed

"""

"""
código com aumento de performace com adições 
import NUMPY-Código que aumeta a velocidade resposta com 'dot',
aumentando sua performace

"""
import numpy as np
e=np.array([1, 7, 3])
d=np.array([0.8, 0.1, 0])
#soma- é reponsável pela somatória entradas *pessos 
def soma(a,b):
     return a.dot(d)

s=soma(e, d)
# a função STEOFUNCTION ativa limiar do perceptron da rede quando maior 1
def stepfunction(soma):
    if (soma>=1):
        return 1
    return 0
funcao=stepfunction(s)