class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        t = list(zip(plantTime, growTime))
        t.sort(key = lambda x: -x[1])
        res, acc_res = 0, 0
        for p,g in t:
            acc_res += p
            res = max(res, acc_res + g)
        return res