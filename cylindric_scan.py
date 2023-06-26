import matplotlib.pyplot as plt
import numpy as np
import math


class Wrapp:
    def __init__(self, func, radius, n, phi):
        self.func = func
        self.radius = 2 * np.pi * radius
        self.x = np.linspace(0, self.radius, 100)
        self.n = n
        self.phi = phi * (np.pi/180)
        self.interceptions = np.empty((0, 2))
        self.linear_points = np.empty((0, 2))

    def create_spirals(self, start_x, height):
        tmp = np.empty((0, 2))
        for j in self.x:
            if start_x == 0:
                f_val = math.tan(self.phi) * j
            else:
                f_val = math.tan(self.phi) * j + abs(self.radius / start_x - self.radius)
            f_val += height
            if f_val <= self.func:
                new_point = np.array([j, f_val])
                self.linear_points = np.vstack((self.linear_points, new_point))
                if j == self.radius:
                    tmp = self.create_spirals(0, f_val)
            else:
                j = 0
                break
        if tmp.size == 0:
            return self.linear_points
        else:
            return np.vstack((self.linear_points, tmp))

    def n_spirals(self):
        mass_point = np.empty((0, 2))
        for i in range(self.n):
            startpoint = self.radius - self.radius/(i+1)
            print(startpoint)
            tmp_i = self.create_spirals(startpoint, 0)
            print(tmp_i)
            mass_point = np.vstack((mass_point, tmp_i))
        return mass_point

    def find_interceptions(self, linear_points):
        unique_points, counts = np.unique(linear_points, axis=0, return_counts=True)
        repeated_points = unique_points[counts > 1]
        self.interceptions = repeated_points
        return self.interceptions

    def plotter(self, points):
        x = points[:, 0]
        y = points[:, 1]
        plt.scatter(x, y)
        plt.show()

    def back_wrapp(self):
        points = self.n_spirals()
        fin_points = np.empty((0,3))
        #for i in points:
# доделать приближение с малой хордой dx и дугой окружности, по идее там приближение будет достаточно



a = Wrapp(10, 3, 2, 20)
print(a)
b = a.n_spirals()
c = a.find_interceptions(b)
d = a.plotter(b)
