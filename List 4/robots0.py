import random
import uuid
import numpy as np
from tabulate import tabulate
import pandas as pd


def random_robot(N):  # 2
    types = ['AUV', 'AFV', 'AGV']

    uid = uuid.uuid4()
    alfanum = uid.hex
    alfanum = alfanum[0:N]

    type = types[random.randint(0, 2)]
    weight = random.randint(50, 2001)
    range = random.randint(1, 1001)
    resolution = random.randint(1, 31)

    return alfanum, type, weight, range, resolution


class robots:  # 1
    def __init__(self, N):
        self.alfanum, self.type, self.weight, self.range, self.resolution = random_robot(
            N)

    def get(self):
        return [self.alfanum, self.type, self.weight, self.range, self.resolution]


def create_robots(M):  # 3
    result = []
    for _ in range(0, M):
        N = random.randint(4, 16)
        tmp_object = robots(N)
        result.append(tmp_object.get())
    return result


def show_robots(robots):  # 4
    robots = np.array(robots)
    print(tabulate(robots, headers=[
          'alfanum', 'type', 'weight', 'range', 'resolution'], tablefmt='orgtbl'))


def split_data(robots):
    result = {}
    for robot in robots:
        result.setdefault('alfanum', []).append(robot[0])
        result.setdefault('type', []).append(robot[1])
        result.setdefault('weight', []).append(robot[2])
        result.setdefault('range', []).append(robot[3])
        result.setdefault('resolution', []).append(robot[4])
    return result


def save(robots): # 5
    robots = split_data(robots)
    df = pd.DataFrame({'alfanum': robots['alfanum'],
                       'type': robots['type'],
                       'weight': robots['weight'],
                       'range': robots['range'],
                       'resolution': robots['resolution']})
    df.to_csv('robots.csv', index=False)


def load(filename): # 5
    return pd.read_csv(filename)


if __name__ == '__main__':
    print('How many robots? : ',end='')
    M = int(input())
    robots = create_robots(M)
    print(robots)
    save(robots)

    # show_robots(robots)
    # loaded = load('robots.csv')
    # print(loaded)
