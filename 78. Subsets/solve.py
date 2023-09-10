class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.subsets = []
        self.stack = []
        n = len(nums)

        def construct(i):
            if i == n :
                self.subsets.append(self.stack.copy())
                return
            construct(i+1)
            self.stack.append(nums[i])
            construct(i+1)
            self.stack.pop()

        construct(0)
        return self.subsets