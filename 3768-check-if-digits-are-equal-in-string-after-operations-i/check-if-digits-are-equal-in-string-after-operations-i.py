class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = [int(digit) for digit in s]
        while len(digits) > 2:
            newS = []
            for pos in range(0, len(digits) - 1):
                pairSum = digits[pos] + digits[pos + 1]  # Use digits, not s
                newS.append(pairSum % 10)
            digits = newS  # Update digits, not s

        return digits[0] == digits[1]  # Compare digits, not s