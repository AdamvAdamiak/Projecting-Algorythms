import random
import uuid
import numpy as np
from tabulate import tabulate
import pandas as pd
from operator import itemgetter
import re
from matplotlib import pyplot as plt
from robots0 import create_robots


def binary_search(item_list, item):
    first = 0
    last = len(item_list)-1
    found = False
    while(first <= last and not found):
        mid = (first + last)//2
        if item_list[mid] == item:
            found = True
            result = item_list.index(item)
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    if found == False:
        return None
    return result


def sort_robots(robots, choice):
    return sorted(robots, key=itemgetter(choice))


def binary_search_robots(robots):
    def get_data_from_user():
        print('0 - Alfanum, 1 - Type, 2 - Weight, 3 - Range, 4 - Resolution')

        print('Choose option: ', end='')

        choice = int(input())

        return choice

    def get_parameters_data_from_user():
        print('Search parameter: ', end='')
        param = int(input())
        return param

    choice = get_data_from_user()

    sorted_robots = sort_robots(robots, choice)

    choiced_tab = []

    for robot in sorted_robots:
        choiced_tab.append(int(robot[choice]))

    param = get_parameters_data_from_user()

    found_elems = []

    for i in range(len(choiced_tab)):
        index = binary_search(choiced_tab, param)
        if index == None:
            continue
        result = sorted_robots[index]
        found_elems.append(result)
        choiced_tab.pop(index)
    return found_elems


def binary_search_robots2(robots):
    def get_data_from_user():
        print('2 - Weight, 3 - Range, 4 - Resolution')

        print('Choose option: ', end='')

        choice = int(input())

        return choice

    def get_parameters_data_from_user():
        print('Search start parameter: ', end='')
        param_start = int(input())

        print('Search end parameter: ', end='')
        param_end = int(input())

        params = []

        for i in range(param_start, param_end+1):
            params.append(i)
        return params

    choice = get_data_from_user()

    params = get_parameters_data_from_user()

    found_elems = []

    sorted_robots = sort_robots(robots, choice)

    choiced_tab = []

    for robot in sorted_robots:
        choiced_tab.append(int(robot[choice]))

    found_elems = []

    print(choiced_tab)
    for param in params:

        param = int(param)
        index = binary_search(choiced_tab, param)
        if index == None:
            continue
        result = sorted_robots[index]
        found_elems.append(result)

    return found_elems


if __name__ == '__main__':
    robots = [['3e39ecf72af446', 'AGV', 1544, 269, 29], ['572fab49b', 'AGV', 1017, 872, 18], ['47dd0618fe9a',
                                                                                     'AUV', 1427, 461, 18], ['139fa922aa2b4', 'AFV', 590, 933, 8], ['bc26500b409d40', 'AFV', 590, 320, 23]]
    print(robots)
    print(binary_search_robots(robots))
    print(binary_search_robots2(robots))
