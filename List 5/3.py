from robots0 import create_robots


def partition(arr, start, end):
    i = start - 1
    pivot = arr[end][choose + 1]
    print_arr.append(arr[end][choose + 1])

    for j in range(start, end):
        if arr[j][choose + 1] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


def quickSort(arr, start, end):
    if start < end:
        p = partition(arr, start, end)
        quickSort(arr, start, p - 1)
        quickSort(arr, p + 1, end)

if __name__ == '__main__':
    robots = create_robots(20)
    print(robots)

    print("1 - mass, 2 - range, 3 - resolution:")
    choose = int(input())
    print_arr = []
    length = len(robots)
    quickSort(robots, 0, length - 1)
    print(f"Result:")
    for robot in robots:
        print(robot)
