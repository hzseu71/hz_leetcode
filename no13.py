class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        pre = 0
        maxAns = 0
        for right,c in enumerate(nums):
            maxAns = max(pre,c+pre)
            pre = max(c+pre,c)
        return maxAns
                     