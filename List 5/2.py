from robots0 import create_robots

data = [['be27efebe87b4b', 'AGV', 1747, 328, 4], ['2eb2', 'AFV', 527, 314, 2], ['4f636d025aeb4b11', 'AUV', 290, 743, 2], [
    'c6becda6090a499', 'AFV', 1691, 810, 8], ['d5275271', 'AFV', 421, 276, 3], ['0ea285f5d4074', 'AFV', 447, 268, 3], ['522a35', 'AUV', 493, 820, 1]]


def countingSort(array):
    size = len(array)
    output = [0] * size

    count = [0] * 10

    for i in range(0, size):
        count[array[i]] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


def get_resolutions(data):
    result = []
    for robot in data:
        result.append(robot[4])
    return result


def print_result(data, sorted_resolutions):
    for r in sorted_resolutions:
        for robot in data:
            if r == robot[4]:
                print(robot)


if __name__ == '__main__':
    robots = data
    resolutions = get_resolutions(robots)
    countingSort(resolutions)
    print("Sorted robots: ")
    print_result(robots, resolutions)
