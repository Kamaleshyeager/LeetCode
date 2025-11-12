class Solution:
    def minOperations(self, a: List[int]) -> int:
        n = len(a)
        if q:=a.count(1): return n-q
        return next((w+n-2 for w in range(n+1) for i in range(n-w+1) if gcd(*a[i:i+w])==1),-1)