from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        m, n = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, m-1, 0, n-1
        ans = []
        
        while top <= bottom and left <= right:
            # 从左到右
            for j in range(left, right+1):
                ans.append(matrix[top][j])
            top += 1
            
            # 从上到下
            for i in range(top, bottom+1):
                ans.append(matrix[i][right])
            right -= 1
            
            if top <= bottom:
                # 从右到左
                for j in range(right, left-1, -1):
                    ans.append(matrix[bottom][j])
                bottom -= 1
            
            if left <= right:
                # 从下到上
                for i in range(bottom, top-1, -1):
                    ans.append(matrix[i][left])
                left += 1
        
        return ans