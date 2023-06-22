import numpy as np
import math


class Wrapp:
    def __int__(self, func, radius, n, phi):
        self.func = func
        self.radius = 2 * np.pi * radius
        self.x = np.linspace(0, self.radius, 10000)
        self.linear_functions = np.empty(0, 0)
        self.intersections = np.empty(0, 0)
        self.n = n
        self.phi = phi * (np.pi/180)

    def generate_surface(self, func, radius):
                x_start = np.linspace(0, self.radius / 2, 10000)
                height = max(self.func(x_start))

    def generate_spirals(self, func, radius, n, phi, height):
        start_points_x = np.linspace(0, self.radius, self.n)
        x = np.linspace(0, self.radius, 10000)
        for i in range(self.n+1):
            row = ([])
            for j in range(x):
                while math.tan(self.phi) * j + self.radius - (self.radius / (i+1)) < max(self.func):
                    new_point = np.array([j, abs(math.tan(self.phi) * j + self.radius - (self.radius / i))])
                    row = np.vstack(row, new_point)
                    if j == self.radius:
                        self.generate_spirals(self.func, self.radius, self.n, self.phi, math.tan(self.phi) * j +
                                              self.radius - (self.radius / (i+1)))
                    self.linear_functions = np.append(self.linear_functions, row, axis=0)
                else:
                    break
        return self.linear_functions

