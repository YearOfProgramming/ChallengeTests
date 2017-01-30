"""
You are given two sorted arrays, A and B, where A has a large enough buffer at the
end to hold B.Write a method to merge B into A in sorted order.

Must run in O(n) time and O(1) space
"""
def sort(arr1, arr2):
    end_arr1 = len(arr1)-len(arr2)-1
    end_arr2 = len(arr2)-1
    buffer_zone_end = len(arr1)-1

    while end_arr1 >= 0 and end_arr2 >= 0:
        if arr1[end_arr1] > arr2[end_arr2]:
            arr1[buffer_zone_end] = arr1[end_arr1]
            end_arr1 -= 1
            buffer_zone_end -= 1
        else:
            arr1[buffer_zone_end] = arr2[end_arr2]
            buffer_zone_end -= 1
            end_arr2 -= 1

    if end_arr1 == -1:
        while end_arr2 != -1:
            arr1[buffer_zone_end] = arr2[end_arr2]
            buffer_zone_end -= 1
            end_arr2 -= 1
    return arr1




print(sort([0, 0, 0, 0], [1, 2, 4, 5]))