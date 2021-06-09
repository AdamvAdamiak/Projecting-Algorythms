import sys


class Node():
    def __init__(self, item):
        self.item = item
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1


class RedBlackTree():  # 1
    def __init__(self):
        self.Node = Node(0)
        self.Node.color = 0
        self.Node.left = None
        self.Node.right = None
        self.root = self.Node

    def helper_delete(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.right_rotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.right.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0

    def swap(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def helper_delete_node(self, node, key):  # 3
        z = self.Node
        while node != self.Node:
            if node.item == key:
                z = node

            if node.item <= key:
                node = node.right
            else:
                node = node.left

        if z == self.Node:
            print("Nie można znaleźć klucza w drzewie")
            return

        y = z
        y_original_color = y.color
        if z.left == self.Node:
            x = z.right
            self.swap(z, z.right)
        elif (z.right == self.Node):
            x = z.left
            self.swap(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.swap(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.swap(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:
            self.helper_delete(x)

    def helper_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right

                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def helper_print(self, node, indent, last):
        if node != self.Node:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.item) + "(" + s_color + ")")
            self.helper_print(node.left, indent, False)
            self.helper_print(node.right, indent, True)

    def preorder(self):
        self.helper_pre_order(self.root)

    def inorder(self):
        self.helper_in_order(self.root)

    def postorder(self):
        self.helper_post_order(self.root)

    def searchTree(self, k):
        return self.helper_search_tree(self.root, k)

    def minimum(self, node):
        while node.left != self.Node:
            node = node.left
        return node

    def maximum(self, node):
        while node.right != self.Node:
            node = node.right
        return node

    def left_rotate(self, x):  # 3
        y = x.right
        x.right = y.left
        if y.left != self.Node:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):  # 3
        y = x.left
        x.left = y.right
        if y.right != self.Node:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):  # 3
        node = Node(key)
        node.parent = None
        node.item = key
        node.left = self.Node
        node.right = self.Node
        node.color = 1

        y = None
        x = self.root

        while x != self.Node:
            y = x
            if node.item < x.item:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.item < y.item:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        self.helper_insert(node)

    def delete_node(self, item):  # 3
        self.helper_delete_node(self.root, item)

    def print_tree(self):
        self.helper_print(self.root, "", True)


if __name__ == "__main__":
    bst = RedBlackTree()
    print('== Dodawanie elementów ==')
    bst.insert(12)
    bst.insert(14)
    bst.insert(75)
    bst.insert(15)
    bst.insert(98)
    bst.insert(48)

    bst.print_tree()

    print("== Usuwanie elementu 14 ==")
    bst.delete_node(14)
    bst.print_tree()
