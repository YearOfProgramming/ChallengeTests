"""
Imagine you are reading in a stream of integers.
Periodically, you wish to be able to look up the rank of a number x
(the number of values less than or equal to x).
Imple-ment the data structures and algorithms to support these operations.
That is,imple-ment the method track(int x), which is called when each number is
generated, and the method get RankOf'Number (int x), which returns the
numberof values less than or equal to x (not including x itself).
"""
class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None


    def track(self, x):
        self.root = self.__insert(x, self.root)

    def __insert(self, x, root):
        if root is None:
            return self.Node(x)
        if root.data < x:
            root.right = self.__insert(x, root.right)
        elif root.data >= x:
            root.left = self.__insert(x, root.left)
        return root

    def get_rank_of_number(self, x):
        return self.get_rank(x, self.root)

    def get_rank(self, x, root):
        print('here')
        if root is None:
            return 0
        if root.data < x:
            print("here2")
            return self.get_rank(x, root.right)
        if root.data > x:
            return self.get_rank(x, root.left)
        if root.data == x:
            return self.get_children(root.left)

    def get_children(self, root):
        if root is None:
            return 0
        else:
            return self.get_children(root.left) + self.get_children(root.right) + 1


bst = BST()
bst.track(5)
bst.track(4)
bst.track(3)
bst.track(4)
bst.track(2)
bst.track(1)
print(bst.get_rank_of_number(4))