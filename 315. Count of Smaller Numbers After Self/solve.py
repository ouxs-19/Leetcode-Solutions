class Solution(object):
    def countSmaller(self, nums):
        count, new = [], sorted(nums)
        for num in nums :
            ind = bisect_left(new,num)
            count.append(ind)
            new.pop(ind)
        return count