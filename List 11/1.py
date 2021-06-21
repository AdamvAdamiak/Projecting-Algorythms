from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GLUT import glutInit
import numpy as np
from numpy import ones, vstack
from numpy.linalg import lstsq
import tkinter as tk
import warnings
a = 0
warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")


def create_list_of_intersections(vector):
    list = []
    for i in range(len(vector)):
        for j in range(len(vector)):
            if i > j:
                k = ((((vector[j][0] - vector[i][0]) * (vector[j][3] - vector[j][1])) - (
                    (vector[j][2] - vector[j][0]) * (vector[j][1] - vector[i][1]))) / (
                    ((vector[i][2] - vector[i][0]) * (vector[j][3] - vector[j][1])) - (
                        (vector[j][2] - vector[j][0]) * (vector[i][3] - vector[i][1]))))
                dxAP = k * (vector[i][2] - vector[i][0])
                dyAP = k * (vector[i][3] - vector[i][1])

                xP = vector[i][0] + dxAP
                yP = vector[i][1] + dyAP

                if min(vector[i][0], vector[i][2]) <= xP <= max(vector[i][0], vector[i][2]) and min(vector[i][1],
                                                                                        vector[i][3]) <= yP <= max(
                        vector[i][1], vector[i][3]):
                    if min(vector[j][0], vector[j][2]) <= xP <= max(vector[j][0], vector[j][2]) and min(vector[j][1],
                                                                                            vector[j][3]) <= yP <= max(
                            vector[j][1], vector[j][3]):
                        list.append([xP, yP])

    return list


def define_point_and_vec_right(vector):
    list = []
    point = (np.random.uniform(-100, 100), np.random.uniform(-100, 100))
    for i in range(len(vector)):
        points = [(vector[i][0], vector[i][1]), (vector[i][2], vector[i][3])]
        x_coords, y_coords = zip(*points)
        alpha = vstack([x_coords, ones(len(x_coords))]).T
        m, c = lstsq(alpha, y_coords)[0]

        if vector[i][1] > vector[i][3] and vector[i][0] > vector[i][2]:
            if -m * point[0] + point[1] - c > 0:
                print('')
                list.append(vector[i])
            if -m * point[0] + point[1] - c < 0:
                print('')
        elif vector[i][1] > vector[i][3] and vector[i][0] < vector[i][2]:
            if -m * point[0] + point[1] - c < 0:
                print('')
                list.append(vector[i])
            if -m * point[0] + point[1] - c > 0:
                print('')
        elif vector[i][1] < vector[i][3] and vector[i][0] < vector[i][2]:
            if -m * point[0] + point[1] - c < 0:
                print('')
                list.append(vector[i])
            if -m * point[0] + point[1] - c > 0:
                print('')
        elif vector[i][1] < vector[i][3] and vector[i][0] > vector[i][2]:
            if -m * point[0] + point[1] - c > 0:
                print('')
                list.append(vector[i])
            if -m * point[0] + point[1] - c < 0:
                print('')

    return point, list


def create_random_vector():
    vector = []
    for i in range(4):
        x = np.random.uniform(-100, 100)
        vector.append(x)
    return vector


def get_data_from_user():
    global a
    print('Zdefiniuj ilość wektorow:', end='')
    x = input()
    a = x
    list = []
    for i in range(int(x)):
        list.append(create_random_vector())
    return list


if __name__ == '__main__':
    vector = get_data_from_user()

    przec = create_list_of_intersections(vector)

    point_cords, vec_right = define_point_and_vec_right(vector)

    root = tk.Tk()
    root.title(f'=== Program działa dla {a} wektorów ===')
    text1 = tk.Text(root, height=30, width=120)
    text1.insert(tk.INSERT, f'Wektory: {vector}\n')
    text1.insert(tk.INSERT, f'Miejsca przecięć wektorów {przec}\n')
    text1.insert(tk.INSERT, f'Ilość przecięć: {len(przec)}\n')
    text1.insert(tk.INSERT, f'Współrzędne punktu: {point_cords}\n')
    text1.insert(
        tk.INSERT, f'Wektory majace punkt po prawej stronie: {vec_right}\n')
    text1.insert(
        tk.INSERT, f'Ilość wektorów mających punkt po prawej stronie: {len(vec_right)}\n')
    text1.pack()
    root.mainloop()


def glut_logic():
    glClear(GL_COLOR_BUFFER_BIT)

    glPointSize(10.0)
    glBegin(GL_POINTS)
    for i in range(len(vector)):
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f(vector[i][2], vector[i][3])

    for i in range(len(przec)):
        glColor3f(0.0, 0.0, 1.0)
        glVertex2f(przec[i][0], przec[i][1])

    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(point_cords[0], point_cords[1])

    glEnd()
    glLineWidth(3)
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    for i in range(len(vector)):
        glVertex2f(vector[i][0], vector[i][1])
        glVertex2f(vector[i][2], vector[i][3])

    glEnd()
    glFlush()


glutInit()
glutInitWindowSize(600, 600)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"Zadanie 1")
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutDisplayFunc(glut_logic)
glutIdleFunc(glut_logic)
glClearColor(1.0, 1.0, 1.0, 1.0)
gluOrtho2D(-100.0, 100.0, -100.0, 100.0)
glutMainLoop()
