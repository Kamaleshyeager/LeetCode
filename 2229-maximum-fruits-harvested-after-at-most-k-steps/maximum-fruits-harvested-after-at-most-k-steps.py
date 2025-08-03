from bisect import bisect_left, bisect_right

class Solution(object):
    def maxTotalFruits(self, fruits, startPos, k):
        """
        :type fruits: List[List[int]]
        :type startPos: int
        :type k: int
        :rtype: int
        """
        positions = [pos for pos, _ in fruits]
        prefix = [0]
        for _, amt in fruits:
            prefix.append(prefix[-1] + amt)

        def get_sum(left_idx, right_idx):
            return prefix[right_idx + 1] - prefix[left_idx]

        n = len(fruits)
        max_total = 0

        # Case 1: Go left first, then right
        for steps_left in range(k + 1):
            left = startPos - steps_left
            right = startPos + max(0, k - 2 * steps_left)
            l_idx = bisect_left(positions, left)
            r_idx = bisect_right(positions, right) - 1
            if l_idx <= r_idx:
                max_total = max(max_total, get_sum(l_idx, r_idx))

        # Case 2: Go right first, then left
        for steps_right in range(k + 1):
            right = startPos + steps_right
            left = startPos - max(0, k - 2 * steps_right)
            l_idx = bisect_left(positions, left)
            r_idx = bisect_right(positions, right) - 1
            if l_idx <= r_idx:
                max_total = max(max_total, get_sum(l_idx, r_idx))

        return max_total
