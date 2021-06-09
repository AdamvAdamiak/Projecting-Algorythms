from functions import *
random.seed(12)


class BSTNode:  # 2
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    def delete(self, val):
        if self == None:
            return self
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)

        if self.right == None:
            return False
        return self.right.exists(val)


def get_robot_data(r_list, p):
    if p == 1:
        return get_weight(r_list)
    elif p == 2:
        return get_range(r_list)
    elif p == 3:
        return get_resolution(r_list)


if __name__ == '__main__':
    robots = create_robots(10)
    show_robots(robots)
    print()
    print('Wybierz parametr: 1 - masa, 2 - zasięg, 3 - rozdzielczość: ', end='')
    param = int(input())
    nodes = get_robot_data(robots, param)
    print('Dane: ', nodes, '\n')
    bst = array_to_bst(nodes)  # 1
    bst.display()
    bst.delete(9)
    print('== Usuwam 9 ==')
    bst.display()
    print('== Dodaje 37 ==')
    bst.insert(37)
    bst.display()

    print('\n')

    print('Kolejność [INORDER]: ', bst.depthFirstSearch_INorder())
    print()
    print('Kolejność [PREORDER]:', bst.depthFirstSearch_PREorder())
    print()
    print('Kolejność [POSTORDER]:', bst.depthFirstSearch_POSTorder())
