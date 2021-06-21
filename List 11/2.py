import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
from math import pi, sin, cos


def draw_triangle(triangle_vertex_1, triangle_vertex_2, triangle_vertex_3):
    plt.plot([0, 0], [-15, 15])
    plt.plot([-15, 15], [0, 0])
    plt.plot([triangle_vertex_1[0], triangle_vertex_2[0], triangle_vertex_3[0], triangle_vertex_1[0]], [
             triangle_vertex_1[1], triangle_vertex_2[1], triangle_vertex_3[1], triangle_vertex_1[1]])
    plt.show()


def is_point_in_triangle(triangle_vertex_1, triangle_vertex_2, triangle_vertex_3, x_1, y_1):
    x_cord = np.array([[triangle_vertex_2[0]-triangle_vertex_1[0], triangle_vertex_3[0]-triangle_vertex_1[0]],
                       [triangle_vertex_2[1]-triangle_vertex_1[1], triangle_vertex_3[1]-triangle_vertex_1[1]]])
    y_cord = np.array([x_1-triangle_vertex_1[0], y_1-triangle_vertex_1[1]])
    z_cord = np.linalg.solve(x_cord, y_cord)

    alfa, beta = z_cord

    if alfa >= 0 and beta >= 0 and alfa+beta <= 1:
        return 1
    else:
        return 0


def do_rotation(triangle_vertex_1, triangle_vertex_2, triangle_vertex_3, alpha, x_0=0, y_0=0):
    x_cord, y_cord = [triangle_vertex_1[0], triangle_vertex_2[0], triangle_vertex_3[0]], [
        triangle_vertex_1[1], triangle_vertex_2[1], triangle_vertex_3[1]]
    alpha = alpha * pi / 180
    for i in range(len(x_cord)):
        x_cord_old = x_cord.copy()
        x_cord[i] = (x_cord[i]-x_0)*cos(alpha) + \
            (y_cord[i]-y_0)*sin(alpha) + x_0
        y_cord[i] = -(x_cord_old[i]-x_0)*sin(alpha) + \
            (y_cord[i]-y_0)*cos(alpha) + y_0

    triangle_vertex_1, triangle_vertex_2, triangle_vertex_3 = [
        x_cord[0], y_cord[0]], [x_cord[1], y_cord[1]], [x_cord[2], y_cord[2]]
    return triangle_vertex_1, triangle_vertex_2, triangle_vertex_3


def animate(i):
    global triangle_vertex_1, triangle_vertex_2, triangle_vertex_3, x_0, y_0
    plt.clf()
    triangle_vertex_1, triangle_vertex_2, triangle_vertex_3 = do_rotation(
        triangle_vertex_1, triangle_vertex_2, triangle_vertex_3, 10, x_0, y_0)

    plt.plot([0, 0], [15, 15])
    plt.plot([15, 15], [0, 0])

    plot_logic()


def plot_logic():
    if is_point_in_triangle(triangle_vertex_1, triangle_vertex_2, triangle_vertex_3, x_1, y_1):
        plt.plot(x_1, y_1, 'o', color='red')
    else:
        plt.plot(x_1, y_1, 'o', color='gray')
    plt.plot([triangle_vertex_1[0], triangle_vertex_2[0], triangle_vertex_3[0], triangle_vertex_1[0]], [
             triangle_vertex_1[1], triangle_vertex_2[1], triangle_vertex_3[1], triangle_vertex_1[1]])


def animate_triangle():
    ani = FuncAnimation(plt.figure(0), func=animate, interval=50)
    plt.show()


if __name__ == "__main__":
    triangle_vertex_1, triangle_vertex_2, triangle_vertex_3 = [
        6, 4], [2, 6], [5, 8]
    [x_0, y_0] = [-10, 10]
    x_1, y_1 = 5.33, 8.96
    # x_1, y_1 = -10, 10

    animate_triangle()
