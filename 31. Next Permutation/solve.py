class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        l = len(nums)
        last = nums[-1]
        i = l-2
        while i>=0 and  last <= nums[i]:
            last = nums[i]
            i-=1
        if i == -1 :
            return nums.reverse()
        j = l-1
        while nums[j]<=nums[i]:
            j-=1
        nums[i],nums[j] = nums[j], nums[i]
        i = i+1
        j = l-1
        while i<j:
            nums[i],nums[j] = nums[j], nums[i]
            i+=1
            j-=1
                        