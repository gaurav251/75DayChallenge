class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = 0
        for val in nums:
            totalSum+=val

        for i in range(len(nums)):
            leftSum = sum(nums[:i])
            if (leftSum * 2) == (totalSum - nums[i]):
                return i

        return -1