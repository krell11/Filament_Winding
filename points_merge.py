import numpy as np
import matplotlib.pyplot as plt

from scipy.spatial import KDTree


def near_points(points):
    kdtree = KDTree(points)
    results = np.empty((0, 3))
    merged_points = set()
    for i, point in enumerate(points):
        if i not in merged_points:
            distance, indices = kdtree.query(point, k=2)
            nearest_point = points[indices[1]]
            percent_diff = calculate_percent_difference(point, nearest_point)
            if percent_diff <= 0.549: # надо более детально смотреть какое значение пока что 0.55 самое оптимальное что смог найти
                merged_points.add(indices[1])
                merged_point = merge_points(point, nearest_point)
                results = np.vstack((results, merged_point))
    return results


def calculate_percent_difference(point1, point2):
    differences = [abs(point1[i] - point2[i]) for i in range(3)]
    differences = np.array(differences)
    average_difference = (sum(differences * differences))**(1/3)
    return average_difference


def merge_points(point1, point2):
    merged_point = tuple(sum(coords) / 2 for coords in zip(point1, point2))
    return merged_point
