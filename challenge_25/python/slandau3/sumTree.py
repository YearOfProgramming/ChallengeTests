import pprint
import random
"""
Youare given a binary tree in which each node contains a value. Design an
algo-rithm to print all paths which sum to a given value.
The path does not need to start or end at the root or a leaf.
There can be negative values
"""

class BinarySearchTree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

        def __repr__(self):
            return str(self.data)

    def __init__(self):
        self.root = None
        self.size = 0
        self.lst = []
    def __increment_size(self):
        self.size += 1

    def __decrement_size(self):
        self.size -= 1

    def insert(self, data):
        self.root = self.__insert(data, self.root)
        self.__increment_size()

    def __insert(self, data, root):
        if root is None:
            return self.Node(data)
        elif root.data < data:
            root.right = self.__insert(data, root.right)
        elif root.data > data:
            root.left = self.__insert(data, root.left)
        return root

    def remove(self, data):
        self.root = self.__remove(data, self.root)
        self.__decrement_size()

    def __remove(self, data, root):
        if root.data == data:
            if root.left is None and root.right is None:
                return None
            else:
                if root.left is not None:
                    root.data = self.get_max(root.left).data
                    root.left = self.__remove(root.data, root.left)
                elif root.right is not None:
                    root.data = self.get_min(root.right).data
                    root.right = self.__remove(root.data, root.right)

        else:
            if root.data < data:
                root.right = self.__remove(data, root.right)
            elif root.data > data:
                root.left = self.__remove(data, root.left)

        return root

    def get_max(self, root):
        if root.right is None:
            return root
        else:
            return self.get_max(root.right)

    def get_min(self, root):
        if root.left is None:
            return root
        else:
            return self.get_min(root.left)

    def is_bst(self):
        return self.__is_bst(self.root)

    def __is_bst(self, root):
        if root is None:
            return True
        if root.left is not None:
            if root.left.data > root.data:
                return False
        if root.right is not None:
            if root.right.data < root.data:
                return False

        return self.__is_bst(root.left) and self.__is_bst(root.right)

    def __len__(self):
        return self.size

    def __contains__(self, item):
        return self.__has_item(item, self.root)

    def __has_item(self, item, root):
        if root is None:
            return False
        if root == item:
            return True
        if root.left is not None and root.left.data > item:
            return self.__has_item(item, root.left)
        if root.right is not None and root.right.data < item:
            return self.__has_item(item, root.right)

    def __add__(self, other):
        while other.size != 0:
            self.insert(other.root)
            other.remove(other.root)
        return self

    def __deepcopy__(self, memodict={}):
        new_bst = BinarySearchTree()
        new_bst.size = self.size
        new_bst.root = self.Node(self.root.data)
        new_bst.root = self.__deepcopy(self.root, new_bst.root)
        return new_bst

    def __deepcopy(self, root, copy_root):
        if root is None:
            return
        if root.left is not None:
            copy_root.left = self.Node(root.left.data)
            self.__deepcopy(root.left, copy_root.left)
        if root.right is not None:
            copy_root.right = self.Node(root.right.data)
            self.__deepcopy(root.right, copy_root.right)
        return copy_root

    def __copy__(self):
        return self.__deepcopy__()  # I don't see a reason why you would need a shallow copy for this

    def __iter__(self):
        # TODO, once I create a queue class
        pass

    def path_to_sum(self, root, target, path): # MAIN CHALLENGE CODE
        if root is None:
            return
        total = sum(path)
        if total == target:
            print(path)
        if root.left is not None:
            if root.left.data + total > target:
                return
            else:
                self.path_to_sum(root.left, target, path+[root.left.data])
        if root.right is not None:
            if root.right.data + total > target:
                return
            else:
                self.path_to_sum(root.right, target, path+[root.right.data])


bt = BinarySearchTree()
bt.insert(10)
bt.insert(15)
bt.insert(9)
bt.insert(6)
bt.path_to_sum(bt.root, 25, [bt.root.data])