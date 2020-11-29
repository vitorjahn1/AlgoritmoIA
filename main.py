# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from queue import PriorityQueue

import pandas as pd
import easygui
import numpy as np

# Press the green button in the gutter to run the script.
from numpy.core._multiarray_umath import arange


def main():
    return easygui.fileopenbox()


def entrega_eficiente(entregasTable):
    aux = 0
    entregasTable
    print(table)
    valorMaximo = []
    for x in range(0,3):
        valorMaximo.append(int(entregasTable[x][2]))

    valor = np.array(valorMaximo).max()
    entrega = ""
    for x in range(0,len(matrizEntregas)):
        if int(matrizEntregas[x][2]) == valor:
                entrega = matrizEntregas[x][0:]
                break

    return entrega


def dataFrameInput(name):
    return pd.read_csv(name)


def proxima_entrega(objetivo):

    for x in arange(0,len(matrizEntregas)-1):
        listaEntrega = []
        if matrizEntregas[x][1] == objetivo[1]:
            listaEntrega = matrizEntregas[x+1][0:]
            return listaEntrega
    listaEntrega = [-1]
    return listaEntrega



def busca(raiz, objetivo,):
    q = PriorityQueue()
    custo = 0
    tempo = objetivo[0]
    q.put((custo,raiz,[raiz]))

    while not q.empty():
        listaCidade = []
        listaCidade = q.get()
        cidade = listaCidade[1]

        if cidade == objetivo[1]:
            custoTotal = calcular_entrega(listaCidade[2])
            print("Tempo :{} ".format(custoTotal*2))
            print("Caminho : {}".format(listaCidade[2]))
            print("Lucro : {}".format(objetivo[2]))

            listaTotal.append(int(objetivo[2]))
            listaEntrega = proxima_entrega(objetivo)
            for x in arange(len(matrizEntregas)-1):
                if int(listaEntrega[0]) == -1:
                    print("Lucro Total : {}".format(sum(listaTotal)))
                    return
                if (custoTotal*2)+int(objetivo[0]) <= int(listaEntrega[0]):
                    return busca('A',listaEntrega)
                else:
                    return busca('A',proxima_entrega(listaEntrega))
            print("Lucro Total : {}".format(sum(listaTotal)))
            return

        cidades_ad = deliveryCidades[cidade]

        for cidade_ad,custoCidade in cidades_ad.items():
            if listaCidade[2].count(cidade_ad):
                continue

            else:
                q.put((custoCidade, cidade_ad, listaCidade[2] + [cidade_ad]))
                custo = int(custoCidade)+ custo


def calcular_entrega(rota):
    valor_da_rota = 0
    for x in arange(0,len(rota)-1):
        valor_da_rota = int(deliveryCidades[rota[x]][rota[x+1]])+valor_da_rota
    return valor_da_rota


table = pd.read_csv('C:/Users/vitor/Downloads/entrada-trabalho - complexa - entrada 2 - entrada-trabalho - complexa - entrada 2 (1).csv')
print(table.columns[0])

print(table.to_numpy())
tableMatriz = table.to_numpy()
print(tableMatriz[1][0])
nuberOFVetex = int(table.columns[0])
aphabet = ['A', 'B', 'C', 'D','E','F','G','H','I','J']
interationNumber = 0
lista = [1, 2, 3]

listaDelivery = []
deliveryCidades = {}
for x in range(1, nuberOFVetex + 1):
    v = np.array(tableMatriz[x][:nuberOFVetex])
    v = list(v)
    cidades={}
    count = 0
    for i in v:
        if int(i) != 0:
            cidades[aphabet[count]] = i
        count = count + 1
    deliveryCidades[aphabet[x - 1]] = cidades

numberOfDelirery = int(tableMatriz[nuberOFVetex + 1][0])
print(deliveryCidades)

for x in range(nuberOFVetex + 2, nuberOFVetex + 2 + numberOfDelirery):
    listaAux = np.array(tableMatriz[x][:3])
    listaAux = list(listaAux)
    listaDelivery.append(listaAux)

print(listaDelivery)

matrizEntregas = np.array(listaDelivery).reshape(numberOfDelirery, 3)

entregaAinda = True



listaTotal = [0]
objetivoLista = entrega_eficiente(matrizEntregas)
busca('A',objetivoLista)



print(matrizEntregas)
