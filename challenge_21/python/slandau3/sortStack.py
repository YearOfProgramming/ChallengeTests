#!/usr/bin/env python3
# Reverse a stack using at most one other stack
def sort_stack(stack):
    utility_stack = []

    while len(stack) != 0:
        temp = stack.pop()
        while len(utility_stack) > 0 and utility_stack[-1] > temp:
            stack.append(utility_stack.pop())
        utility_stack.append(temp)

    return utility_stack

print(sort_stack([5,4,3,2,1]))