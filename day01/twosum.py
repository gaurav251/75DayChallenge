def twoSum(nums, target):

    # This one uses hash_map or dictionary

    n = len(nums)
    hash_map = {}
    for i in range(n):
        first = nums[i]
        second = target - first
        if second in hash_map:
            return [i, hash_map[second]]  # if found in the map then return the location
        else:
            hash_map[nums[i]] = i  # if not present in the map then add to it


print(twoSum(nums=[2, 7, 11, 15], target=9))
print("-" * 20)
print(twoSum(nums=[3, 2, 4], target=6))
print("-" * 20)
print(twoSum(nums=[3, 3], target=6))
print("-" * 20)
