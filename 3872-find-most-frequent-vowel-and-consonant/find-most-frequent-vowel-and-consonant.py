class Solution:
    def maxFreqSum(self, s: str) -> int:
        mask=0x104111
        maxCV=[0]*2
        freq=[0]*26
        for c in s:
            x=ord(c)-97
            idx=((1<<x) & mask)!=0
            freq[x]+=1
            maxCV[idx]=max(maxCV[idx], freq[x])
        return maxCV[0]+maxCV[1]
        