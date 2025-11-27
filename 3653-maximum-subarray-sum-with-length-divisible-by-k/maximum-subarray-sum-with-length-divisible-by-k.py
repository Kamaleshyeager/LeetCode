class Solution:
    def maxSubarraySum(self, a: List[int], k: int) -> int:
        p = [0,*accumulate(a)]
        return max(max(accumulate(map(sub,p[i+k::k],p[i::k]),
            lambda q,v:max(v,q+v),initial=-inf)) for i in range(k))