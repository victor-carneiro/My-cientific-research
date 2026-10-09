# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 23:22:15 2026

@author: Cristina
"""
import numpy as np
import matplotlib.pyplot as plt
def plotar(vetor_v, m, n1):
    t_vetor = np.linspace(1/m, 1, m)   # instantes de tempo
    for i in range(n1):
        plt.plot(t_vetor, vetor_v[i], alpha=0.05, color='blue')
    plt.xlabel("t")
    plt.ylabel("B(t)")
    plt.title(f"Movimento Browniano com Drift (M={m})")
    plt.show()
    
def Browniano(n1):
    vetor_v10    = np.zeros((n1, 10))
    vetor_v100   = np.zeros((n1, 100))
    vetor_v1000  = np.zeros((n1, 1000))
    vetor_v10000 = np.zeros((n1, 10000))
    lista = [10, 100, 1000, 10000]
    (a, b, c) = (1, 2, 3)

    for m in lista:
        if m == 10:
            vetor_a = vetor_v10
        elif m == 100:
            vetor_a = vetor_v100
        elif m == 1000:
            vetor_a = vetor_v1000
        else:
            vetor_a = vetor_v10000

        dt = 1/m
        t_vetor = np.linspace(dt, 1, m)
        Y = np.random.choice([-1, 1], size=(n1, m))
        W = np.cumsum(np.sqrt(dt) * Y, axis=1)
        vetor_a[:] = a * t_vetor + b + c * W

    plotar(vetor_v10,    10,    n1)
    plotar(vetor_v100,   100,   n1)
    plotar(vetor_v1000,  1000,  n1)
    plotar(vetor_v10000, 10000, n1)

Browniano(1000)

#Parte 2

def Z_Browniano(n1):
    vetor_v10    = np.zeros((n1, 10))
    vetor_v100   = np.zeros((n1, 100))
    vetor_v1000  = np.zeros((n1, 1000))
    vetor_v10000 = np.zeros((n1, 10000))
    lista = [10, 100, 1000, 10000]
    (a, c) = (1, 3)
    for m in lista:
        if m == 10:
            vetor_a = vetor_v10
        elif m == 100:
            vetor_a = vetor_v100
        elif m == 1000:
            vetor_a = vetor_v1000
        else:
            vetor_a = vetor_v10000
        dt=1/m
        t_vetor = np.linspace(dt, 1, m)

        # sorteia todos os Y de uma vez: matriz (n1 x m)
        Y = np.random.choice([-1, 1], size=(n1, m))

        # cada incremento: a*dt + c*sqrt(dt)*Y
        incrementos = a*dt + c*np.sqrt(dt)*Y

        # variação quadrática acumulada: soma dos quadrados ao longo dos passos
        vetor_a[:] = np.cumsum(incrementos**2, axis=1)

    # plot
    for vetor_a, m in zip([vetor_v10, vetor_v100, vetor_v1000, vetor_v10000], lista):
        t_vetor = np.linspace(1/m, 1, m)
        plt.figure()
        for i in range(n1):
            plt.plot(t_vetor, vetor_a[i], alpha=0.05, color='blue')
        # reta limite determinista c²t
        plt.plot(t_vetor, c**2 * t_vetor, color='red', linewidth=2, label=f'$c^2 t = {c**2}t$')
        plt.xlabel("t")
        plt.ylabel("ξ(t)")
        plt.title(f"Variação Quadrática (M={m})")
        plt.legend()
        plt.show()

Z_Browniano(1000)
    