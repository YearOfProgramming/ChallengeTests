"""
Given a sorted array of strings which is interspersed with empty strings,
write a method to find the location of a given string.
Must run in logN time
"""


def find(lst, target, s=0, m=0, e=0):
    start = s
    mid = m
    end = e

    if lst[start] == '':
        for i in range(len(lst)):
            if i != '':
                start = i
                break

    if lst[mid] == '':
        left = mid
        right = mid
        while left != 0 or right != len(lst):
            if lst[left] != '':
                mid = left
                break
            elif lst[right] != '':
                mid = right
                break
            left -= 1
            right += 1

    if lst[end] == '':
        for i in range(len(lst)-1,mid,-1):
            print(i)
            if i != '':
                end = i
                break

    if lst[start] == target:
        return start
    elif lst[mid] == target:
        return mid
    elif lst[end] == target:
        return end

    if ord(target) < ord(lst[mid]):
        end = mid
        mid = mid//2
        return find(lst, target, start, mid, end)
    else:
        start = mid
        mid += mid//2
        return find(lst, target, start, mid, end)

a = ['a', 'b', '', '', 'c', '', 'd', '', 'f']

print(find(a, 'b', 0, len(a)//2, len(a)-1))