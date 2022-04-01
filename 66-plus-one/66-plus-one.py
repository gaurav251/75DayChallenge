class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
   
        carry = 1
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] == 9 and carry == 1:
                digits[i], carry = 0, 1
            else:
                digits[i], carry = digits[i] + carry, 0
        if carry:
            digits.insert(0, 1)
        return digits