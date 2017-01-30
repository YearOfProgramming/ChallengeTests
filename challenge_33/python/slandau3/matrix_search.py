"""Given a m * n matrix, find the coordinates of a given number inside that matrix.
The algorithm must be faster than O(n^2).
The matrix will be sorted whereas position 0,0 will be the smallest number in the matrix
and the bottom right will be the largest (ascending order left to right, top to bottom)."""
def find(mat, target, rowstart=0, rowmid=0, rowend=0):
    colstart = 0
    print()
    print(rowstart)
    print(rowmid)
    print(rowend)
    print()
    if mat[rowstart][0] <= target <= mat[rowstart][len(mat[rowstart])-1]:
        # target is in this row
        print("here1")
        colmid = len(mat[rowstart]) // 2
        colend = len(mat[rowstart]) - 1
        return rowstart, bsearch(mat[rowstart], target, colstart, colmid, colend)
    elif mat[rowmid][0] <= target <= mat[rowmid][len(mat[rowend])-1]:
        # target is in this row
        print("here2")
        colmid = len(mat[rowmid])//2
        colend = len(mat[rowmid])-1
        return rowmid, bsearch(mat[rowmid], target, colstart, colmid, colend)
    elif mat[rowend][0] <= target <= mat[rowend][len(mat[rowend])-1]:
        # taret is in this row
        print("here3")
        colmid = len(mat[rowend])//2
        colend = len(mat[rowend])-1
        return rowend, bsearch(mat[rowend], target, colstart, colmid, colend)

    if target < mat[rowmid][0]:
        # in one of the top rows
        print("here4")
        rowend = rowmid
        rowmid = rowmid//2
        return find(mat, target, rowstart, rowmid, rowend)
    else:
        # in bottom rows
        print("here5")
        rowstart = rowmid+1
        rowmid += rowmid//2
        return find(mat, target, rowstart, rowmid, rowend)

def bsearch(lst, target, s=0, m=0, e=0):
    if lst[s] == target:
        return s
    elif lst[m] == target:
        return m
    elif lst[e] == target:
        return e

    if target < lst[m]:
        e = m
        m = m//2
        return bsearch(lst, target, s, m, e)
    else:
        s = m+1
        m += m//2
        return bsearch(lst, target, s, m, e)

mat = [[0, 1, 2, 3, 4],
       [5, 6, 7, 8, 9],
       [10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19],
       [20, 21, 22, 23, 24],
       [25, 26, 27, 28, 29]]

print(find(mat, 3, 0, len(mat)//2, len(mat)-1))