class Solution:
    def trap(self, height: List[int]) -> int:
        # ans = 0
        # for i in range(len(height)):
        #     max_left = 0
        #     max_right = 0
        #     for k in range(i):
        #         if height[k]>height[i]:
        #             max_left = max(height[k],max_left)
        #     for j in range(i+1,len(height)):
        #         if height[j]>height[i]:
        #             max_right = max(height[j],max_right)
        #     v_i = min(max_left,max_right) - height[i]
        #     ans += max(0, v_i)
        # return ans
        if not height:
            return 0
        left,right = 0,len(height)-1
        left_max = right_max = 0
        ans = 0
        while left<right:
            if height[left]<height[right]:
                if height[left]>=left_max:
                    left_max = height[left]
                else:
                    ans += left_max-height[left]
                left+=1
            else:
                if height[right]>=right_max:
                    right_max = height[right]
                else:
                    ans += right_max-height[right]
                right-=1
        return ans