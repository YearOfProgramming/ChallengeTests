"""Is a the given binary tree a binary search tree?"""

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

    def insert(self, data):
        self.root = self.__insert(data, self.root)

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

    def printall(self, root):
        if root is None:
            return
        print(root.data)

        self.printall(root.left)
        self.printall(root.right)

    def isBST(self, root):
        if root is None:
            return True
        if root.left is not None:
            if root.left.data > root.data:
                return False
        if root.right is not None:
            if root.right.data < root.data:
                return False

        return self.isBST(root.left) and self.isBST(root.right)

bst = BinarySearchTree()
bst.insert(5)
bst.insert(4)
bst.insert(3)
bst.insert(6)
bst.insert(7)
bst.insert(6.6)
bst.insert(4.5)
print(bst.isBST(bst.root))

bst.root.left.left.left = bst.Node(1000)  # manually putting a node in
print(bst.isBST(bst.root))