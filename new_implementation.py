import matplotlib.pyplot as plt
import numpy as np
import math

np.set_printoptions(suppress=True)


class Wrapp:
    def __init__(self, height, r, phi, n, clearance):
        self.height = height
        self.phi = phi
        self.clearance = clearance
        self.r = r
        self.r_pi = r * 2 * np.pi
        self.x = np.linspace(0, self.r * 2 * np.pi, self.clearance)
        self.points_on_plane = np.empty((0, 2))
        self.theta = np.linspace(0, 2*np.pi, self.clearance)
        self.n = n

    def h_calc(self, phi):
        h = self.r_pi * math.sin(phi)
        return h

    def period_calc(self):
        return math.ceil(self.height / self.h_calc(self.phi))

    def create_spirals(self, coordinates, step):
        points = np.empty((0, 3))
        total_height = 0
        angle = 0
        while total_height <= self.height:
            x = round(self.r * math.cos(angle + coordinates), 5)
            y = round(self.r * math.sin(angle + coordinates), 5)
            z = abs(round(angle * self.h_calc(self.phi), 5))
            total_height = z
            if total_height >= self.height:
                break
            point = np.array([[x, y, z]])
            points = np.vstack((points, point))
            angle += step
        return points

    def plotter_cylindric_shape(self, points):
        points = np.array(points)
        x = points[:, 0]
        y = points[:, 1]
        z = points[:, 2]
        min_height = np.min(z)
        min_height_indices = np.where(z == min_height)[0]
        colors = ['blue'] * len(x)
        for index in min_height_indices:
            colors[index] = 'red'
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x, y, z)
        plt.show()

    def calculate_angles(self, n):
        angles = []
        for i in range(n):
            angles.append(abs(self.r_pi/n*i - self.r_pi))
        return angles

    def calculate_start_coordinates(self, angles):
        x = []
        y = []
        for angle in angles:
            x.append(self.r * np.cos(angle))
            y.append(self.r * np.sin(angle))
        return np.column_stack((x, y))

    def create_multiple_spirals(self):
        spirals = np.empty((0, 3))
        spirals1 = np.empty((0, 3))
        start_points = self.calculate_angles(self.n)
        # start_points = self.calculate_start_coordinates(self.calculate_angles(self.n)) не работает
        for i in range(self.n):
            spiral = self.create_spirals(start_points[i], 0.04)
            spirals = np.vstack((spirals, spiral))
            spiral1 = self.create_spirals(start_points[i], -0.04)
            spirals1 = np.vstack((spirals1, spiral1))
        combined_spirals = np.vstack((spirals, spirals1))
        return combined_spirals
