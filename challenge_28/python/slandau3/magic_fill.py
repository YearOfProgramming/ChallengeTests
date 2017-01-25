import pprint
"""
Implement the "paint fill" function that one might see on many image editing programs.
That is, given a screen (represented by a two-dimensional array of colors),
a point, and a new color, fill in the surrounding area until the color changes from the original color
"""
mat = [[2, 2, 2, 2],
       [2, 3, 3, 2],
       [2, 3, 3, 3],
       [3, 2, 2, 2]]
# N^4 ?
def magic_fill(x, y, color_shift, val_to_change):
    if x >= len(mat) or y >= len(mat) or x < 0 or y < 0:
        return
    elif mat[y][x] == val_to_change:
        mat[y][x] = color_shift
        magic_fill(x+1, y, color_shift, val_to_change)
        magic_fill(x-1, y, color_shift, val_to_change)
        magic_fill(x, y+1, color_shift, val_to_change)
        magic_fill(x, y-1, color_shift, val_to_change)
    else:
        return
magic_fill(1,1,4,mat[1][1])
for i in mat:
    print(i)