

def findSum(input: list):
    lst = []
    max = 0
    for i in range(len(input)):
        total = 0
        temp = []
        for j in range(i, len(input)):
            total += input[j]
            temp.append(input[j])
            if total > max:
                max = total
                lst = temp.copy()
    print(max)
    return lst

print(findSum([-8, 3, -2, -3, -6, 4, -10]))