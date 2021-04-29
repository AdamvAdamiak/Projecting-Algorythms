import random
import uuid
import numpy as np
from tabulate import tabulate
import pandas as pd
from operator import itemgetter
import re
from matplotlib import pyplot as plt
from robots0 import create_robots

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
            choice = str(input())
            if choice == '':
                choice = None
            else:
                choice = int(choice)
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
        choice = str(input())

        if choice == '':
            user_choices.append(None)
        else:
            choice = int(choice)
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
    robots = create_robots()
    print(robots)
    robots = convert_to_tuple(robots)
    hashed_robots = hash_robots(robots)  # 2
    print('Robot with index ',hash_search(robots))
    print('Robot with index ', search_by_2_params(robots))
