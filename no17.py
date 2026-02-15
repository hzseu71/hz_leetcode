class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashtable = dict()
        for c in nums:
            if c>0:
                hashtable[c] = 1
        k = 1
        while k>0:
            if k in hashtable:
                k+=1
                continue

            return k
        