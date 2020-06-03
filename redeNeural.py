# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 16:48:10 2020

@author: FELIPE_MOHAMED!
"""
# -*- coding: utf-8 -*-

entradas=[1,7,5]
pesos=[0.8, 0.1, 0]

def soma(e , p):
    valor=0
    for i in range(3):
        valor+= e[i]  *  p[i]
       
    return valor

somatorio=soma(entradas, pesos)
def steofunction (soma):
    if (soma>=1):
        return 1
    return 0
funcao=steofunction(somatorio)
    