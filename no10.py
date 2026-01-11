class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        cur = 0
        ans = 0
        for x in nums:
            cur+=x
            ans+=count.get(cur-k,0)
            count[cur] += 1
        return ans
