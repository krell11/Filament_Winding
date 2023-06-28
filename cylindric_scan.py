import matplotlib.pyplot as plt
import numpy as np
import math


class Wrapp:
    def __init__(self, func, radius, n, phi):
        self.func = func
        self.radius = 2 * np.pi * radius
        self.x = np.linspace(0, self.radius, 10)
        self.n = n
        self.phi = phi * (np.pi/180)
        self.interceptions = np.empty((0, 2))
        self.linear_points = np.empty((0, 2))
        self.point_for_projection = np.empty((0, 3))
        self.theta = []

    def create_spirals(self, start_x, height):
        tmp = np.empty((0, 2))
        for j in self.x:
            if start_x == 0:
                f_val = math.tan(self.phi) * j
            else:
                f_val = math.tan(self.phi) * j + (self.radius / start_x - self.radius)
            f_val += height
            if f_val <= self.func:
                new_point = np.array([j, f_val])
                self.linear_points = np.vstack((self.linear_points, new_point))
                self.theta.append(j / self.radius)
                if j == self.radius:
                    tmp = self.create_spirals(0, f_val)
            else:
                break
        if tmp.size == 0:
            return self.linear_points
        else:
            return np.vstack((self.linear_points, tmp))

    def n_spirals(self):
        mass_point = self.linear_points
        for i in range(self.n):
            startpoint = self.radius - self.radius/(i+1)
            tmp_i = self.create_spirals(startpoint, 0)
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

    def plotter_cylindric_shape(self, points):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xlim(left=-a.radius, right=a.radius)
        ax.set_ylim(bottom=0, top=a.func)
        x = points[:, 0]
        y = points[:, 1]
        z = points[:, 2]
        ax.scatter(x, y, z)
        plt.show()

    def project_points_to_cylinder_side(self):
        z = self.create_spirals(0, 0)
        for i in range(len(self.linear_points)):
            theta_value = self.theta[i]
            x = self.radius*np.cos(theta_value)/(2*np.pi)
            y = self.radius*math.sin(theta_value)/(2*np.pi)
            z_i = z[i, 1]
            tmp = np.array([x, y, z_i])
            self.point_for_projection = np.vstack((self.point_for_projection, tmp))
        return self.point_for_projection


a = Wrapp(10, 3, 1, 2)
print(a)
c = a.project_points_to_cylinder_side()
d = a.n_spirals()
a.plotter_cylindric_shape(c)
a.plotter(d)
