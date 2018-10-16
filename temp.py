# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""
import math
import random
from scipy.stats import norm, chi2
import matplotlib.pyplot as graph

y=0.5
itersForEachN = 10
maxN = 1000


def hiPoints():
    res = []
    for i in range(1, maxN):
        sum3 = 0
        for _ in range(itersForEachN):
            sum2 = sum([norm.rvs(0, 1) ** 2 for _ in range(i)])
            d1 = 1 / (chi2.ppf((1 - y) / 2, i))
            d2 = 1 / (chi2.ppf((1 + y) / 2, i))
        sum3 += (sum2 * (d1 - d2))
        res.append(sum3 / 1)
    return res

def normPoints():
    res = []
    for i in range(1, maxN):
        sum3 = 0
        for _ in range(itersForEachN):
            sum2 = i * ((sum([norm.rvs(0, 1) for _ in range(i)]) / i) ** 2)
            d1 = 1 / ((norm.ppf((3 - y) / 4)) ** 2)
            d2 = 1 / ((norm.ppf((3 + y) / 4)) ** 2)
            sum3 += (sum2 * (d1 - d2))
        res.append(sum3 / itersForEachN)
    return res
if __name__ == "__main__":

    graph.clf()
    graph.plot([i for i in range(1, maxN)], hiPoints())
    graph.savefig("hi2.png")

    graph.clf()
    graph.plot([i for i in range(1, maxN)], normPoints())
    graph.savefig("norm.png")
