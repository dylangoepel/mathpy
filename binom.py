# approximate the binomial distribution the binomial distribution

def binom(a, b):
    p = 1
    for i in range(a - b + 1, a + 1):
        p *= i
    for i in range(1, b + 1):
        p //= i
    return p

def plotBinom(samples):
    x, y = binomGraph(samples)
    plt.plot(x, y)
