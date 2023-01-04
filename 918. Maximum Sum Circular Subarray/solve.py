class Solution(object):
    def maxSubarraySumCircular(self, nums):
        n = len(nums)
        max_sum = float("-inf")
        min_sum = float("inf")
        max_sum_var = 0
        arr_sum = 0
        min_sum_var = 0
        for i in range(n):
            max_sum_var += nums[i]
            min_sum_var += nums[i]
            arr_sum += nums[i]
            max_sum = max_sum_var if max_sum < max_sum_var else max_sum
            min_sum = min_sum_var if min_sum > min_sum_var else min_sum
            if max_sum_var < 0:
                max_sum_var = 0
            if min_sum_var > 0:
                min_sum_var = 0
        if arr_sum == min_sum_var:
            return max_sum
        return max(max_sum, arr_sum - min_sum)