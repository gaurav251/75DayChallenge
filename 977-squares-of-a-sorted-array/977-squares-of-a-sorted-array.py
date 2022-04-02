class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # nums is soreted in increasing order
        squares = [num ** 2 for num in nums]  # Generating squares
        i, j = 0, len(nums) - 1
        resultant = []
        while i <= j:
            a, b = squares[i], squares[j]
            resultant.insert(0, max(a, b))
            if a > b:
                i += 1
            else:
                j -= 1

        return resultant