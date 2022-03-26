def twoSum(nums, target):
    size = len(nums)

    for i in range(size):
        first = nums[i]
        second = target - first

        if second in nums[i + 1 :]:
            j = nums[i + 1 :].index(second)
            break

    return [i, i + j + 1]


print(twoSum(nums=[2, 7, 11, 15], target=9))
print("-" * 20)
print(twoSum(nums=[3, 2, 4], target=6))
print("-" * 20)
print(twoSum(nums=[3, 3], target=6))
print("-" * 20)
