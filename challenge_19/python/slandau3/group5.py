def chosen(start, nums, target):
    print(nums)
    if nums[start - 1] == target:
        return True
    elif start == len(nums):
        return False
    else:
        for i in range(start, len(nums)):
            nc = nums[:]
            if i == 0:
                continue

            nc[i] = nc[i] + nc[i - 1]
            if nums[i] == 1 and nums[i - 1] - nums[i] % 5 == 0:
                return
            if chosen(start + 1, nc, target):
                return True
        return False


print(chosen(0, [2,7,5,1,3,1,4,9], 14))
