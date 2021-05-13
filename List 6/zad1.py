from random import randint

HEAP_NUMBER = 8


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) == 0

    def insert(self, data, priority):
        self.queue.append([data, priority])

    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i][1] > self.queue[max][1]:
                    max = i
            item = self.queue[max][0]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()

    def search(self, item):
        for ele in self.queue:
            if ele[0] == item:
                return f'{item} is found'
        return 'Not found'


class Binary_heap_quene(object):

    def __init__(self):
        self.H = [0]*(HEAP_NUMBER+1)
        self.size = -1

    def parent(self, i):

        return (i - 1) // 2

    def leftChild(self, i):

        return ((2 * i) + 1)

    def rightChild(self, i):

        return ((2 * i) + 2)

    def shiftUp(self, i):

        while (i > 0 and self.H[self.parent(i)] < self.H[i]):

            self.swap(self.parent(i), i)

            i = self.parent(i)

    def shiftDown(self, i):

        maxIndex = i

        l = self.leftChild(i)

        if (l <= self.size and self.H[l] > self.H[maxIndex]):

            maxIndex = l

        r = self.rightChild(i)

        if (r <= self.size and self.H[r] > self.H[maxIndex]):

            maxIndex = r

        if (i != maxIndex):

            self.swap(i, maxIndex)
            self.shiftDown(maxIndex)

    def insert(self, p):

        self.size = self.size + 1
        self.H[self.size] = p

        self.shiftUp(self.size)

    def extractMax(self):

        result = self.H[0]

        self.H[0] = self.H[self.size]
        self.size = self.size - 1

        self.shiftDown(0)
        return result

    def changePriority(self, i, p):
        oldp = self.H[i]
        self.H[i] = p

        if (p > oldp):

            self.shiftUp(i)

        else:

            self.shiftDown(i)

    def getMax(self):
        return self.H[0]

    def Remove(self, i):
        self.H[i] = self.getMax() + 1

        self.shiftUp(i)

        self.extractMax()

    def swap(self, i, j):
        temp = self.H[i]
        self.H[i] = self.H[j]
        self.H[j] = temp

    def get(self):
        return self.H

    def search(self, item):
        for ele in self.H:
            if ele == item:
                return f'{item} is found'
        return 'Not found'

    def test(self):
        i = 0

        print("Priority Queue : ", end="")
        while (i <= self.size):

            print(self.H[i], end=" ")
            i += 1

        print()

        print("Node with maximum priority :",  self.extractMax())

        print("Priority queue after extracting maximum : ", end="")
        j = 0
        while (j <= self.size):

            print(self.H[j], end=" ")
            j += 1

        print()

        self.changePriority(2, 251)
        print("Priority queue after priority change at index 2 to 251 : ", end="")
        k = 0
        while (k <= self.size):

            print(self.H[k], end=" ")
            k += 1

        print()

        self.Remove(3)
        print("Priority queue after removing the element with index 3 : ", end="")
        l = 0
        while (l <= self.size):

            print(self.H[l], end=" ")
            l += 1
        print()
        print('Search value: ', end='')
        print(self.search(int(input())))


def create_priority_data():
    i = 0
    data = []
    while i <= 30:
        data.append([randint(0, 1000), i])
        i += 3
    return data


def append_data_to_object(object, data):
    for line in data:
        object.insert(line[0], line[1])

def append_data_to_heap_object(object):
    for i in range(HEAP_NUMBER):
        line = randint(0, 1000)
        object.insert(line)


def test_queue():
    Queue = PriorityQueue()
    data = create_priority_data()
    append_data_to_object(Queue, data)
    print('Data [data,priority]: ',Queue)
    print('Search value: ', end='')
    print(Queue.search(int(input())))
    print(f'Removing item with highest priority: {Queue.delete()}')
    print('Data [data,priority] after removing item: ',Queue)


def test_heap_queue():
    heapQueue = Binary_heap_quene()
    append_data_to_heap_object(heapQueue)
    heapQueue.test()


if __name__ == '__main__':
    print('=== TEST QUEUE ===')
    test_queue()
    print('=== TEST BINARY HEAP QUEUE ===')
    test_heap_queue()
