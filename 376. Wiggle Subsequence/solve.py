class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n, i = len(nums), 1
        while i < n and nums[i] == nums[i-1]: i += 1
        if i == n: return 1
        up, ans = nums[i-1] > nums[i], 1
        while i < n:
            if (up and nums[i] < nums[i-1]) or (not up and nums[i] > nums[i-1]):
                up = not up
                ans += 1
            i += 1
        return ans