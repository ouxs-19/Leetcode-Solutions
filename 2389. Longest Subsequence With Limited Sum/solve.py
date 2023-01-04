class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        res = []
        for q in queries:
            tres = 0
            cnt = 0 
            for num in nums :
                tres += num
                cnt += 1
                if tres > q :
                    cnt -= 1
                    break
            res.append(cnt)
        return res