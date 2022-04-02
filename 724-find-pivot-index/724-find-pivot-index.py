class Solution:
    """
    -----------------
    This was developed by some other dude
    -----------------
    """
    def pivotIndex(self, nums: List[int]) -> int:
        sum_left, sum_right = 0, sum(nums[1:])

        for i in range(len(nums) - 1):
            if sum_left == sum_right:
                return i
            sum_left += nums[i]
            sum_right -= nums[i + 1]
        
        if sum_left == sum_right:
            return len(nums) - 1
        
        return -1