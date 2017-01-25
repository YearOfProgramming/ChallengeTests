#!/usr/bin/env python3

from collections import deque
import random

"""
An animal shelter holds only dogs and cats, and operates on a strictly
"first in, first out" basis. People must adopt either the "oldest"
(based on arrival time) of all animals at the shelter, or
they can select whether they would prefer a dog or a cat
(and will receive the oldest animal of that type).
They cannot select which specific animal they would like.
Create the data structures to maintain this system and
implement opera-tions such as enqueue, dequeueAny, dequeueDog and dequeueCat.
You may use the built-in L inkedL ist data structure.
"""

DOG = 0
CAT = 1

catQ = deque()
dogQ = deque()
bothQ = deque()


def insertAnimal(type):
    if type == DOG:
        dogQ.append(DOG)  # append, appends to the tail
    else:
        catQ.append(CAT)
    bothQ.append(type)


def getCat():
    bothQ_holder = []
    first = bothQ.pop()
    while first != CAT:
        bothQ_holder.append(first)
        first = bothQ.pop()

    while len(bothQ_holder) != 0:
        bothQ.appendleft(bothQ_holder.pop())  # BQ holder will be in reverse order in which the list was popped
        # meaning that when we pop it all back to the head of the queue it will be in perfect order
    return catQ.pop()


def getDog():
    bothQ_holder = []
    first = bothQ.pop()
    while first != DOG:
        bothQ_holder.append(first)
        first = bothQ.pop()

    while len(bothQ_holder) != 0:
        bothQ.appendleft(bothQ_holder.pop())

    return dogQ.pop()


def getAny():
    type = bothQ.pop()
    if type == DOG:
        dogQ.pop()
    else:
        catQ.pop()
    return type


for i in range(0, 20):
    insertAnimal(random.randint(0, 1))


def printAll():
    print('dog q', dogQ)
    print('cat q', catQ)
    print('both q', bothQ)
    print()


while True:
    inp = input()
    if inp == 'd':
        print(getDog())
        printAll()
    elif inp == 'c':
        print(getCat())
        printAll()
    elif inp == 'a':
        print(getAny())
        printAll()
    else:
        exit()
