# approximate the binomial distribution the binomial distribution

import numpy as np
import matplotlib.pyplot as plt

def binom(a, b):
    p = 1
    for i in range(a - b + 1, a + 1):
        p *= i
    for i in range(1, b + 1):
        p //= i
    return p

def binomGraph(samples):
    step = 1 / samples
    xs = np.arange(0, 1 + step, step)
    ys = xs.copy()
    for i in range(samples):
        ys[i] = binom(samples, i)
    return xs, ys

def plotBinom(samples):
    x, y = binomGraph(samples)
    plt.plot(x, y)

if __name__ == "__main__":
    plotBinom(1000)
    plt.show()
