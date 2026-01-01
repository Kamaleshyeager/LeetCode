class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 1                                               # <-- 1)

        for i in range(len(digits) - 1, -1, -1):                # <-- 2)
            carry, digits[i] = divmod(digits[i] + carry, 10)
            if carry == 0: break

        else: 
            if carry > 0: digits.insert(0, carry) # see Note below.

        return digits