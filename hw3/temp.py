# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""
import math
import random
import matplotlib.pyplot as graph

lam = 152

def uniForK(k):
    sum = 0
    n = 1000
    for _ in range(n):
        sum += random.uniform(0, lam) ** k
        
    return ((k+1) * (sum / n)) ** (1.0/k)

def expForK(k):
    sum = 0
    n = 1000
    for _ in range(n):
        sum += random.expovariate(lam) ** k
        
    return (math.factorial(k) / (sum / n)) ** (1.0/k)

def skoUnif(k):
    repeatNum = 1920
    return (sum([(lam - uniForK(k)) ** 2 for _ in range(repeatNum)]) / repeatNum) ** 0.5

def skoExp(k):
    repeatNum = 1920
    return (sum([(lam - expForK(k)) ** 2 for _ in range(repeatNum)]) / repeatNum) ** 0.5
    
if __name__ == "__main__":
    pntsUnif = []
    pntsExp = []
    
    maxK = 128
    for k in range(1, maxK):
        pntsUnif.append(skoUnif(k))
        pntsExp.append(skoExp(k))

    graph.clf()
    graph.plot([i for i in range(1, maxK)], pntsUnif)
    graph.savefig("uni_1_128.png")

    graph.clf()
    graph.plot([i for i in range(1, maxK)], pntsExp)
    graph.savefig("exp_1_128.png")
