from robots0 import *
import random
import uuid
import numpy as np
from tabulate import tabulate
import pandas as pd
from operator import itemgetter
import re


def binary_search(item_list, item):  # 2
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


def sort_robots(robots):  # 1
    print('0 - Alfanum, 1 - Type, 2 - Weight, 3 - Range, 4 - Resolution')

    print('Choose option: ', end='')

    choice = int(input())

    sorted_robots = sorted(robots, key=itemgetter(choice))

    choiced_tab = []

    for robot in sorted_robots:
        choiced_tab.append(int(robot[choice]))

    print('Search parameters(space between numbers): ', end='')
    params = str(input())
    params = re.split(r' ', params)
    found_elems = []

    for param in params:
        param = int(param)
        result = binary_search(choiced_tab, param)
        if result == None:
            continue
        result = sorted_robots[result]

        found_elems.append(result)

    return found_elems


if __name__ == '__main__':
    print('How many robots? : ', end='')
    M = int(input())
    robots = create_robots(M)
    print(robots)
    print(sort_robots(robots))
