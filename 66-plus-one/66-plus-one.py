class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        n = len(digits)
        for i in range(n - 1, -1, -1):
            digits[i] = digits[i] + carry
            digits[i], carry = digits[i] % 10, digits[i] // 10
        if carry:
            digits.insert(0, carry)
        return (digits)