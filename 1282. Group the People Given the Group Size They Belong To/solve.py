class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = []
        dic = defaultdict(list)
        
        for ind, size in enumerate(groupSizes):
            dic[size].append(ind)
            if len(dic[size]) == size:
                res.append(dic[size].copy())
                dic[size] = []

        return res