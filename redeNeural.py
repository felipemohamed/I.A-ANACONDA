
# Created on Thu Jun  4 10:31:30 2020

# @author: FelipeMohamed

# código com aumento de performace com adições 
# import NUMPY-Código que aumeta a velocidade resposta com 'dot',
# aumentando sua performace



''' CÓDIGO QUE TEM MAIOR PERFORMACE SEM IMPORT NUMPY
# entradas=[1,7,5]
# pesos=[0.8, 0.1, 0]
'''
import numpy as np
e=np.array([1, 7, 3])
d=np.array([0.8, 0.1, 0])

def soma(e , p):
    valor=0
   ''' ciclo só com for é possível mais com uma perfomace ruim em grandes dados
   for i in range(3):
    valor+= e[i]  *  p[i]
      return valor
    '''

    def soma(a,b):
     return a.dot(d)
somatorio=soma(entradas, pesos)
def steofunction (soma):
    if (soma>=1):
        return 1
    return 0
funcao=steofunction(somatorio)
    