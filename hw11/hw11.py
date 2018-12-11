# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""

import numpy as np
import matplotlib.pyplot as graph
from collections import defaultdict

N = 100000
a = 3
c = 1.0 / (2 * np.exp(-a) + 2 * a)
d = 0.1
def inverse():
    r = np.random.uniform()
    if r < c * np.exp(-a):   
        return np.log(r / c)
    
    if r < c * (np.exp(-a) + 2 * a):
        return r / c - np.exp(-a) - a

    return np.log(c / (1 - r))

def decomposition():
    r = np.random.uniform()
    
    if r < c * np.exp(-a):
        return np.log(np.random.uniform()) - a
        
    if r < c * (2 * a + np.exp(-a)):
        return np.random.uniform(-a, a)
        
    return a - np.log(np.random.uniform()) 

def plot_buckets(arr, fn):
    counters = defaultdict(int)
    for x in arr:
        counters[np.floor(x / d)] += 1   
            
    items = sorted(counters.items())
    
    a1 = []
    a2 = []
    for i in range(len(items)):
        a1.append(d * items[i][0])
        a2.append(items[i][1])
        
    graph.plot(a1, a2, label=fn)
    graph.savefig(fn)
    graph.close() 
    
if __name__ == "__main__":
    
    arr1 = []
    arr2 = []
    for i in range(N):
        arr1.append(inverse())
        arr2.append(decomposition())
    arr1 = filter(lambda x: abs(x) < 10, arr1)
    arr2 = filter(lambda x: abs(x) < 10, arr2)
    
    plot_buckets(arr1, "inv.png")
    plot_buckets(arr2, "dec.png")
