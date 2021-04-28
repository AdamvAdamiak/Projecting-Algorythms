from robots0 import *
import random
import uuid
import numpy as np
from tabulate import tabulate
import pandas as pd


def linear_search1(robots):
    def get_data_from_user():
        print('0 - Alfanum, 1 - Type, 2 - Weight, 3 - Range, 4 - Resolution')

        print('Choose option: ', end='')
        choice = int(input())

        print('Search parameter: ', end='')
        param = input()
        return choice, param

    choice, param = get_data_from_user()

    for robot in robots:
        if str(robot[choice]) == str(param):
            return robot

    return None


def linear_search2(robots):
    user_choices = []

    def get_data_from_user():
        choices = ['Alfanum', 'Type', 'Weight', 'Range', 'Resolution']
        for i in range(5):
            print(f'Enter {choices[i]}: ', end='')
            choice = str(input())
            if choice == '' or choice.upper() == 'NONE':
                choice = None
            user_choices.append(choice)
    get_data_from_user()
    print(user_choices)
    for robot in robots:
        count = 0
        for i in range(5):
            if str(robot[i]) == str(user_choices[i]):
                count += 1
            if user_choices[i] == None:  # jeśli  None to pomijamy
                count += 1
        if count == 5:  # jesli robot spelni wszystkie 5 porównań jest tym szukanym
            return robot


def linear_search3(robots):
    user_choices = []

    def get_data_from_user():
        choices = ['Alfanum', 'Type', 'Weight', 'Range', 'Resolution']
        for i in range(5):
            print(f'Enter {choices[i]}: ', end='')
            choice = str(input())
            if choice == '' or choice.upper() == 'NONE':
                choice = None
            user_choices.append(choice)
    get_data_from_user()

    for robot in robots:
        count = 0
        for i in range(5):
            if user_choices[i] == None:
                count += 1
            else:
                if str(robot[i]) in user_choices[i]:
                    count += 1
        if count == 5:
            return robot


if __name__ == '__main__':
    print('How many robots? : ', end='')
    M = int(input())
    robots = create_robots(M)
    print(robots)

    # print(linear_search1(robots))

    print(linear_search2(robots))

    # print(linear_search3(robots))
