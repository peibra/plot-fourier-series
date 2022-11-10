from matplotlib import pyplot as plt
import numpy as np


class FourierSeries:
    def zero(self):
        return 0

    def __init__(self, a=zero, b=zero, n=50, start=-8, end=None):
        self.a = a
        self.b = b

        self.n = n

        self.end = end
        if end is None:
            self.end = -start
        self.x = np.arange(start, self.end, 0.1)

    def cos_series(self, x):
        val = 0
        for k in range(self.n+1):
            val += self.a(k) * np.cos(k*x)

        return val

    def sin_series(self, x):
        val = 0
        for k in range(1, self.n+1):
            val += self.b(k) * np.sin(k*x)

        return val

    def f(self, x):
        return self.cos_series(x) + self.sin_series(x)

    def plot(self):
        y = self.f(self.x)
        plt.plot(self.x, y)
        plt.grid()
        plt.show()


# example program below (triangular wave)


def main():
    def b(k):
        return (8/np.pi) / k**2 * np.sin(np.pi * k / 2)

    fs = FourierSeries(b=b)

    fs.plot()


if __name__ == '__main__':
    main()
