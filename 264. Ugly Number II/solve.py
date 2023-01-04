class Solution:
    def nthUglyNumber(self, n: int) -> int: 
        ug_nums = [1]
        base = {2,3,5}
        while len(ug_nums) != n :
            num = min(base)
            ug_nums.append(num)
            base.remove(num)
            base.add(num*2)
            base.add(num*3)
            base.add(num*5)
        return ug_nums[-1]