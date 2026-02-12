class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = []
        n = len(nums)
        start = n-1-k
        while len(temp) != n:
            temp.append(nums[start%n])
            start+=1
        nums[:] = temp
        