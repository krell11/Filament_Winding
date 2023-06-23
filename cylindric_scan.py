import numpy as np
import math


class Wrapp:
    def __init__(self, func, radius, n, phi):
        self.func = func
        self.radius = 2 * np.pi * radius
        self.x = np.linspace(0, self.radius, 10000)
        self.n = n
        self.phi = phi * (np.pi/180)
        self.interceptions = np.empty((0, 2))

    def create_spirals(self, func, radius, n, phi, height):
        linear_points = np.empty((0, 2))
        for i in range(self.n):
            for j in self.x:
                f_val = math.tan(self.phi) * j + abs(self.radius / (i + 2) - self.radius)
                if f_val <= self.func:
                    new_point = np.array([j, f_val])
                    linear_points = np.vstack((linear_points, new_point))
                    if j == self.radius:
                        self.create_spirals(func, radius, n, phi, f_val)
                else:
                    break
        return linear_points

    def find_interceptions(self, linear_points):
        for i in range(len(linear_points)):
            for j in range(i + 1, len(linear_points)):
                if linear_points[i] == linear_points[j]:
                    self.interceptions = np.vstack(self.interceptions, linear_points[i])
        return self.interceptions

