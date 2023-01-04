class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.somme = sum(nums)
        self.bar = len(nums)//2

    def update(self, index: int, val: int) -> None:
        self.somme -= self.nums[index]
        self.somme += val
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        if right - left > self.bar :
            return self.somme - sum(self.nums[:left]) - sum(self.nums[right + 1:])
        return sum(self.nums[left: right + 1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)