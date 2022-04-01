class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string_digits = ""
        for value in digits:
            string_digits += str(value)
        int_digits = int(string_digits) + 1
        string_digits = str(int_digits)
        return [int(i) for i in string_digits]