class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = nums[0], 0
        for val in nums:
            if val == candidate:
                count += 1
            else:
                count -= 1

            if count < 0:
                candidate, count = val, 0
        return candidate