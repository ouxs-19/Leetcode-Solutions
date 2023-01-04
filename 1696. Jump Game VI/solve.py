from queue import PriorityQueue
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        l = len(nums)
        q = PriorityQueue()
        q.put((-nums[-1],l-1))
        for i in range(l-2,-1,-1):
            while q.qsize()  : 
                elem = q.get()
                if elem[1] <= i+k : 
                    q.put(elem)
                    break
            nums[i] = nums[i]-elem[0]
            q.put((-nums[i],i))
        return nums[0]