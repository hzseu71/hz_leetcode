class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
 
        if not nums or k == 0 or k > len(nums):
            return []
        if k == 1:
            return nums 
        dq = deque()
        ans = []
        for i,v in enumerate(nums):
            while dq and dq[0] <= i-k:
                dq.popleft()
            while dq and nums[dq[-1]] < v:
                dq.pop
            dq.append(i)
            if i>=k-1:
                ans.append(nums[dq[0]])
        return ans     
        