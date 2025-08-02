from collections import Counter

class Solution(object):
    def minCost(self, basket1, basket2):
        count = Counter(basket1) + Counter(basket2)
        if any(v % 2 for v in count.values()):
            return -1  # Impossible to make both equal
        
        # Get how many are extra in each basket
        delta = Counter(basket1) - Counter(basket2)
        delta += Counter(basket2) - Counter(basket1)
        
        # Only half of the extra elements need to be swapped
        extra = []
        for k in delta:
            extra += [k] * (abs(delta[k]) // 2)
        
        extra.sort()
        min_val = min(count)  # cheapest fruit in both baskets

        # Pair the most expensive with the cheapest to minimize cost
        total = 0
        for i in range(len(extra) // 2):
            total += min(2 * min_val, extra[i])
        return total
