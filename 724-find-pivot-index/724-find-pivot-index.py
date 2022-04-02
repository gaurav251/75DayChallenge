class Solution:
    # def pivotIndex(self, nums: List[int]) -> int:
    def pivotIndex(self, nums):
        totalSum = sum(nums)

        for i in range(len(nums)):
            leftSum = sum(nums[:i])
            if (leftSum * 2) == (totalSum - nums[i]):
                return i
        return -1