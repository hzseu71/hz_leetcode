class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # numbers = dict()
        # max = 0
        # sorted_nums = sorted(set(nums))
        # for n in sorted_nums:
        #     if n-1 in numbers:
        #         numbers[n] = numbers[n-1] + 1
        #     else:
        #         numbers[n] = 1
        #     if numbers[n] > max:
        #         max = numbers[n]
        # return max
        max = 0
        num_set = set(nums)
        max = 1
        for n in num_set:
            if n-1 not in num_set:
                
                current_num = n
                current_len = 1
                while current_num+1 in num_set:
                    current_num+=1
                    current_len+=1
                if current_len > max:
                    max = current_len
        return max