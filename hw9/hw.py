from scipy import optimize
def func(x):
    return (476 - 2020 * (1 - x) ** 2) ** 2 / (2020 * (1 - x) ** 2) + \
        (1017 - 2020 * 2 * x * (1 - x)) ** 2 / (2020 * 2 * x * (1 - x)) + \
        (527 - 2020 * x ** 2) ** 2 / (2020 * x ** 2)

eps = 1e-9
print(optimize.minimize(func, 0.9, bounds=[(0+eps, 1-eps)]))
