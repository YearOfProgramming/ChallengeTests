"""
Given a sorted array of n integers that has been rotated an unknown number of times,
write code to find an element in the array.
You may assume that the array was originally sorted in increasing order.
Must be done in logN time.

The function should return the index of the element
"""

def find(lst, target):
    start = 0
    mid = len(lst)//2
    end = len(lst)-1

    if lst[start] == target:
        return start
    if lst[mid] == target:
        return mid
    if lst[end] == target:
        return end

    if lst[start] < lst[end]: # no rotation
        if target < lst[mid]:
            end = mid
            return find(lst[start:end], target)
        else:
            start = mid+1
            return find(lst[start:end], target)

    elif lst[start] > lst[mid]:
        # left is inflection
        if lst[mid] < target < lst[end]:
            # check to see if it's to the right
            return find(lst[mid:end],target)
        else:
            return find(lst[start:mid],target)
    else:
        if lst[start] < target < lst[mid]:
            # check to see if it's to the left
            return find(lst[start:mid], target)
        else:
            return find(lst[mid:end], target)


lst = [4,5,6,1,2,3]
print(find(lst, 3))
