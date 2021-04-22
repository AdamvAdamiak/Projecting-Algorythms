import random
import uuid
import numpy as np
from tabulate import tabulate
import pandas as pd
from operator import itemgetter
import re
from matplotlib import pyplot as plt


def convert_to_tuple(robots):
    result = []
    for robot in robots:
        result.append(tuple(robot))
    return result


def hash_robots(robots): # 1
    result = []
    for robot in robots:
        result.append(hash(robot))
    return result


def hash_search(robots):
    user_choices = []

    def get_data_from_user():
        choices_str = ['Alfanum', 'Type', ]
        choices_int = ['Weight', 'Range', 'Resolution']
        for i in range(2):
            print(f'Enter {choices_str[i]}: ', end='')
            choice = str(input())
            if choice == '' or choice.upper() == 'NONE':
                choice = None
            user_choices.append(choice)

        for i in range(3):
            print(f'Enter {choices_int[i]}: ', end='')
            choice = int(input())
            if choice == '':
                choice = None
            user_choices.append(choice)
    get_data_from_user()

    user_choices = tuple(user_choices)

    for robot in robots:

        hashed_robot = hash(robot)
        hashed_user_robot = hash(user_choices)

        if hashed_robot == hashed_user_robot:
            return robots.index(robot)
    return None


def search_by_2_params(robots):
    choices = ['Weight', 'Range']  # 2 3
    user_choices = []
    for i in range(2):
        print(f'Enter {choices[i]}: ', end='')
        choice = int(input())

        if choice == '':
            user_choices.append(None)
        user_choices.append(choice)

    count_check = 0
    count_similar = 0
    for robot in robots:
        for i in range(2):
            if user_choices[i] != None:
                count_check += 1
                if hash(robot[i+2]) == hash(user_choices[i]):
                    count_similar += 1
        if count_similar == count_check:
            return robots.index(robot)
    return 'Not found'


if __name__ == '__main__':
    print('How many robots? : ', end='')
    M = int(input())
    robots = [['3e39ecf72af446', 'AGV', 1544, 269, 29], ['572fab49b', 'AGV', 1017, 872, 18], ['47dd0618fe9a',
                                                                                     'AUV', 1427, 461, 18], ['139fa922aa2b4', 'AFV', 590, 933, 8], ['bc26500b409d40', 'AFV', 590, 320, 23]]
    print(robots)
    robots = convert_to_tuple(robots)
    print(robots)
    hashed_robots = hash_robots(robots)  # 2
    print(hash_search(robots))
    print('Robot with index ', search_by_2_params(robots))
