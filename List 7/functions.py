import string
import random


class binarySearchTree:  # 1
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):

        if (self.val == None):
            self.val = val

        else:

            if val == self.val:
                return 'Duplikaty są niemożliwe w drzewie binarnym'  # 4

            if (val < self.val):

                if(self.left):
                    self.left.insert(val)

                else:
                    self.left = binarySearchTree(val)

            else:
                if(self.right):
                    self.right.insert(val)
                else:
                    self.right = binarySearchTree(val)

    def insert_left(self, val):
        self.left = val

    def insert_right(self, val):
        self.right = val

    def depthFirstSearch_INorder(self):
        return self.traverseInOrder([])

    def depthFirstSearch_PREorder(self):
        return self.traversePreOrder([])

    def depthFirstSearch_POSTorder(self):
        return self.traversePostOrder([])

    def traverseInOrder(self, lst):
        if (self.left):
            self.left.traverseInOrder(lst)
        lst.append(self.val)
        if (self.right):
            self.right.traverseInOrder(lst)
        return lst

    def traversePreOrder(self, lst):
        lst.append(self.val)
        if (self.left):
            self.left.traversePreOrder(lst)
        if (self.right):
            self.right.traversePreOrder(lst)
        return lst

    def traversePostOrder(self, lst):
        if (self.left):
            self.left.traversePostOrder(lst)
        if (self.right):
            self.right.traversePostOrder(lst)
        lst.append(self.val)
        return lst

    def findNodeAndItsParent(self, val, parent=None):

        if val == self.val:
            return self, parent
        if (val < self.val):
            if (self.left):
                return self.left.findNodeAndItsParent(val, self)
            else:
                return 'Nie znaleziono'
        else:
            if (self.right):
                return self.right.findNodeAndItsParent(val, self)
            else:
                return 'Nie znaleziono'

    def delete(self, val):

        if(self.findNodeAndItsParent(val) == 'Nie znaleziono'):
            return 'Wierzchołek nie jest w drzewie'

        deleteing_node, parent_node = self.findNodeAndItsParent(val)

        nodes_effected = deleteing_node.traversePreOrder([])

        if (len(nodes_effected) == 1):
            if (parent_node.left.val == deleteing_node.val):
                parent_node.left = None
            else:
                parent_node.right = None
            return 'Usunięto'

        else:

            if (parent_node == None):
                nodes_effected.remove(deleteing_node.val)

                self.left = None
                self.right = None
                self.val = None

                for node in nodes_effected:
                    self.insert(node)
                return 'Usunięto'

            nodes_effected = parent_node.traversePreOrder([])

            if (parent_node.left == deleteing_node):
                parent_node.left = None
            else:
                parent_node.right = None

            nodes_effected.remove(deleteing_node.val)
            nodes_effected.remove(parent_node.val)
            for node in nodes_effected:
                self.insert(node)

        return 'Usunięto'

    def display(self):  # 3
        lines, *_ = self.helper_display()
        for line in lines:
            print(line)

    def helper_display(self):

        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if self.right is None:
            lines, n, p, x = self.left.helper_display()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if self.left is None:
            lines, n, p, x = self.right.helper_display()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self.left.helper_display()
        right, m, q, y = self.right.helper_display()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '' + s + y * '' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def if_bst(self):  # 2
        indicator = 1
        node_list = self.depthFirstSearch_INorder()
        for i in range(0, len(node_list)-2):
            if node_list[i] > node_list[i+1]:
                indicator = 0
                self.delete(node_list[i])
                self.insert(node_list[i])
        if indicator == 1:
            return 'BST sprawdzone'
        else:
            return self.if_bst()


def array_to_bst(array_nums):
    array_nums.sort()
    if not array_nums:
        return None
    mid_num = len(array_nums)//2
    node = binarySearchTree(array_nums[mid_num])
    node.left = array_to_bst(array_nums[:mid_num])
    node.right = array_to_bst(array_nums[mid_num+1:])
    return node


class robot:
    def __init__(self, ID, typ, weight, range, resolution):
        self.ID = ID
        self.typ = typ
        self.weight = weight
        self.range = range
        self.resolution = resolution


def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


typ = ['AUV', 'AFV', 'AGV']


def random_robot():
    typ = ['AUV', 'AFV', 'AGV']
    return id_generator(), random.choice(typ), random.randint(50, 2000), random.randint(1, 1000), random.randint(1, 30)


def create_robots(M):
    vector = []
    for i in range(M):
        rr = random_robot()
        new_robot = robot(rr[0], rr[1], rr[2], rr[3], rr[4])
        vector.append(new_robot)
    return vector


def show_robots(vector):
    print('=== Roboty ===')
    for i in range(len(vector)):
        print(vector[i].ID, vector[i].typ,
              vector[i].weight, vector[i].range, vector[i].resolution)


def get_weight(vec):
    tmp = []
    for i in range(len(vec)):
        tmp.append(vec[i].weight)
    return tmp


def get_range(vec):
    tmp = []
    for i in range(len(vec)):
        tmp.append(vec[i].range)
    return tmp


def get_resolution(vec):
    tmp = []
    for i in range(len(vec)):
        tmp.append(vec[i].resolution)
    return tmp
