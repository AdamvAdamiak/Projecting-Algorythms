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


def create_help_vectors(robots): # 1
    result = {}
    choices_names = ['Alfanum', 'Type', 'Weight', 'Range', 'Resolution']
    choices = [0, 1, 2, 3, 4]
    help_vectors = {}
    for choice in choices:
        result = {}
        print(choices_names[choice])
        for i in range(len(robots)):
            result.setdefault(i, []).append(robots[i][choice])
        print('Initial Values: ',result)
        result = sorted(result, key=result.get)
        print('Help Vector: ',result)
        help_vectors.setdefault(choices_names[choice], []).append(result)
    return help_vectors


def binary_search_robots(robots):
    user_choices = []
    help_vectors = create_help_vectors(robots)

    def get_data_from_user():
        choices = ['Alfanum', 'Type', 'Weight', 'Range', 'Resolution']
        for i in range(5):
            print(f'Enter {choices[i]}: ', end='')
            choice = str(input())
            if choice == '' or choice.upper() == 'NONE':
                choice = None
            user_choices.append(choice)

    def choices():
        found = []
        for robot in robots:
            count = 0
            index = 0
            result = []
            for i in range(len(user_choices)):
                if robot[count] == user_choices[count]:
                    result.append(index)
                elif(user_choices[count] == None):
                    result.append(index)
                count += 1
                index += 1
            if(len(result) != 0):
                found.append(result)
        return found

    get_data_from_user()
    found = choices()
    set1 = set(found[0])
    set2 = set(found[1])
    set3 = set(found[2])
    set4 = set(found[3])
    set4 = set(found[4])
    return set.intersection(set1, set2, set3, set4)


if __name__ == '__main__':
    print('How many robots? : ', end='')
    M = int(input())
    robots = create_robots(M)
    print(robots)
    print(binary_search_robots(robots))
