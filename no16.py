class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # preL = []
        # recL = []
        # tempp=1
        # for c in nums:
        #     tempp *= c
        #     preL.append(tempp)
        # tempr = 1
        # k = len(nums)-1
        # while k > -1:
        #     tempr *= nums[k]
        #     recL.insert(0,tempr)
        #     k -= 1

        # ans = []
        # for c in range(len(nums)):
        #     if c==0:
        #         ans.append(recL[c+1])
        #     elif c==len(nums)-1:
        #         ans.append(preL[c-1])
        #     else:
        #         ans.append(recL[c+1]*preL(c-1))
        
        # return ans

        n = len(nums)
        ans = [1] * n
        # 左侧乘积
        left = 1
        for i in range(n):
            ans[i] = left
            left *= nums[i]
        # 右侧乘积
        right = 1
        for i in range(n-1, -1, -1):
            ans[i] *= right
            right *= nums[i]
        return ans        
