class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        save = {0:0}
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            mod = s % k
            if  mod not in save:
                save[mod] = i + 1
            elif save[mod] < i:
                return True
        return False