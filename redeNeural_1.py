
#Created on Wed Jun  3 16:48:10 2020
#@author: FelipeMohamed

# -*- coding: utf-8 -*-
import numpy as np
entrada=np.array([[0,0],[0,1],[1,0],[1,1]])
pesos=np.array([0.0,0.0]#parte que fará ativção do neurônio
saidas=np.array([0,0,0,1])
taxaDeAprender=0.1

def stepfunction(soma):
    if (soma>=1):
        return 1
    return 0

def calcularAsSaidas(regristro):
   # s=regristro.dot(pesos)
    return stepfunction(regristro.dot(pesos))
# a função a seguir irá treinar a rede
def supervicionar():
    erroTotal=1
    while(erroTotal!=0):
        erroTotal=1
        # analisará o processo de soma e verificará se conver com a saída.
        for i in range((len(saidas))):
            saidaCalculada=calcularAsSaidas(np.asarray(entrada[i]))
            print("saida calculada:"+str(saidaCalculada))
            # verifica de o erro de comparação
            erro=abs(saidas[i]-saidaCalculada)
           
            erroTotal+=erro
            #adiciona novos pessoos até operação dar erro=0, ou seja  saída forem igiaus
            for j in range((len(pesos))):
                pesos[j]= pesos[j]+(taxaDeAprender*erro*entrada[i][j])
                print("valor novo de peso:"+str(pesos[j]))
                
        print("valor do erroTotal tentativa:"+str(erroTotal))

                  
supervicionar()  