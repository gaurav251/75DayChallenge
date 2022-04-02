class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # nums is soreted in increasing order
        squares = [num ** 2 for num in nums]  # Generating squares
        i, j = 0, len(nums) - 1
        resultant = []
        while i <= j:
            if squares[i] >= squares[j]:
                resultant.insert(0, squares[i])
                i += 1
            else:
                resultant.insert(0, squares[j])
                j -= 1

        return resultant