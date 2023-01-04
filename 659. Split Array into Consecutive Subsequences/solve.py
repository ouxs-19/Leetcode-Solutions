class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        seq = defaultdict(int)
        left = Counter(nums)
        
        for num in nums:
            if left[num]:
                if seq[num-1]:
                    seq[num-1] -= 1 
                    seq[num] += 1
                    left[num] -= 1
                else:
                    if not left[num+1] or not left[num+2]: 
                        return False
                    left[num] -= 1
                    left[num+1] -= 1
                    left[num+2] -= 1
                    seq[num+2] += 1

        return True