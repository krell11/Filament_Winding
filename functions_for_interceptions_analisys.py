import numpy as np
from scipy.spatial import KDTree
import matplotlib.pyplot as plt

np.set_printoptions(suppress=True)


def nearest_points(points):
    kdtree = KDTree(points)
    results = []
    for i, point in enumerate(points):
        distance, index = kdtree.query(point, k=2)
        nearest_point = points[index[1]]
        results.append((point, nearest_point, distance[1]))
    return results


def remove_duplicate_points(points):
    unique_points, unique_indices = np.unique(points, axis=0, return_index=True)
    unique_points = points[np.sort(unique_indices)]
    return unique_points


def calculate_mean_dist(array):
    if len(array) > 0:
        mean_value = sum(array) / len(array)
    else:
        mean_value = 0.0
    return mean_value


def filter_points_by_mean(points, mean_distance):
    filtered_points = []
    for point, nearest_point, distance in points:
        if distance <= mean_distance:
            filtered_points.append(point)
    return filtered_points


def find_average_points(points1, points2):
    average_points = []
    combined_points = points1 + points2
    for point_pair in nearest_points(combined_points):
        point1, point2, _ = point_pair
        average_point = [(p1 + p2) / 2 for p1, p2 in zip(point1, point2)]
        average_points.append(average_point)
    return average_points


def clear_massive(arr):
    return arr.reshape(arr.shape[0], -1)


def plot_3d_arrays(red_array, blue_array):
    red_array = np.array(red_array)
    blue_array = np.array(blue_array)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    red_x = red_array[:, 0]
    red_y = red_array[:, 1]
    red_z = red_array[:, 2]
    blue_x = blue_array[:, 0]
    blue_y = blue_array[:, 1]
    blue_z = blue_array[:, 2]
    ax.scatter(red_x, red_y, red_z, c='red', marker='o')
    ax.scatter(blue_x, blue_y, blue_z, c='blue', marker='o')
    plt.show()


def calculate_average_coordinates(points):
    average_coordinates = []
    for pair in points:
        if len(pair) >= 2:
            x1, y1, z1 = pair[:, 0]
            x2, y2, z2 = pair[:, 1]
            average_x = (x1 + x2) / 2
            average_y = (y1 + y2) / 2
            average_z = (z1 + z2) / 2
            average_coordinates.append([average_x, average_y, average_z])
    return average_coordinates
