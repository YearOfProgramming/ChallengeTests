#!/usr/bin/env python3
import random
from collections import deque

"""
Given a binary tree, design an algorithm which creates a linked list of all the nodes at
each depth (e.g., if you have a tree with depth D,you'll have D linked lists).

"""
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.data)

class NodeLL:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        temp = self.head
        if self.head is None:
            self.head = NodeLL(data)
            return
        while temp.next is not None:
            temp = temp.next
        temp.next = NodeLL(data)

    def printAll(self):
        temp = self.head
        while temp is not None:
            print(str(temp.data))
            temp = temp.next



class BinaryTree:
    def __init__(self, data=None):
        self.root = Node(data)

    def insert(self, data):
        self.root = self.__insert(data, self.root)

    def __insert(self, data, root):
        if root is None:
            return Node(data)
        elif root.data < data:
            root.right = self.__insert(data, root.right)
        else:
            root.left = self.__insert(data, root.left)

        return root

def createTree():
    bt = BinaryTree(50)
    for _ in range(100):
            bt.insert(random.randint(0,1000))

    return bt


def list_linkify(btree):
    # Need to do a level order traversal
    currentLevel = deque()
    nextLevel = deque()
    linked_lists = [LinkedList()]
    currentLevel.append(btree.root)

    while len(currentLevel) != 0:
        current = currentLevel.pop()
        linked_lists[-1].insert(current.data)

        if current.left is not None:
            nextLevel.append(current.left)
        if current.right is not None:
            nextLevel.append(current.right)

        if len(currentLevel) == 0:
            if len(nextLevel) == 0:  # if there is nothing in the next leevl. We are done
                break

            currentLevel = nextLevel.copy()
            nextLevel = deque()
            linked_lists.append(LinkedList())

    return linked_lists

bt = createTree()
l = list_linkify(bt)
for i in l:
    i.printAll()
    print()