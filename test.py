import numpy as np
from new_implementation import Wrapp
from functions_for_interceptions_analisys import nearest_points, remove_duplicate_points, calculate_mean_dist\
    , filter_points_by_mean, clear_massive, plot_3d_arrays, calculate_average_coordinates
from points_merge import merge_points,near_points, calculate_percent_difference

a = Wrapp(height=100, r=10, phi=2, n=7, clearance=1000)
b = a.create_multiple_spirals()
a.plotter_cylindric_shape(b)
c = remove_duplicate_points(b)
n_points = nearest_points(b)
mean_distance = calculate_mean_dist([distance for _, _, distance in n_points])
filtered_points = filter_points_by_mean(n_points, mean_distance)
a.plotter_cylindric_shape(filtered_points)
#clear_points = calculate_average_coordinates(filtered_points)
#plot_3d_arrays(filtered_points, b)
#a.plotter_cylindric_shape(filter_points_by_mean(n_points, mean_distance))
nearest_neighbors = near_points(filtered_points)
a.plotter_cylindric_shape(nearest_neighbors)
