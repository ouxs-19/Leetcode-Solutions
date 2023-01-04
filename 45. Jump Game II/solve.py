class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 : return 0 
        if n == 2 : return 1
        
        long, jumps, curr  = (0,0,0)
        
        for i,j in enumerate(nums[:-1]):
            next_pos = i + j
            if next_pos > long : long = next_pos
            if i == curr :
                curr = long
                jumps += 1
        return jumps