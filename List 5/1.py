from random import randint


def data():
    vector = []
    for i in range(10):
        vector.append(i+randint(1, 202))
    return vector


def countingSort(data, pValue):
    countArray = [0] * 10
    inputSize = len(data)

    for i in range(inputSize):
        placeElement = (data[i] // pValue) % 10
        countArray[placeElement] += 1

    for i in range(1, 10):
        countArray[i] += countArray[i-1]

    outputArray = [0] * inputSize
    i = inputSize - 1
    while i >= 0:
        currentEl = data[i]
        placeElement = (data[i] // pValue) % 10
        countArray[placeElement] -= 1
        newPosition = countArray[placeElement]
        outputArray[newPosition] = currentEl
        i -= 1

    return outputArray


def radixSort(data):

    maxEl = max(data)

    i = 1
    while maxEl > 0:
        maxEl /= 10
        i += 1

    pValue = 1

    outputData = data
    while i > 0:
        outputData = countingSort(outputData, pValue)
        pValue *= 10
        i -= 1

    return outputData


if __name__ == '__main__':
    input = data()
    print('before sort ', input)
    sorted = radixSort(input)
    print('after sort ', sorted)
