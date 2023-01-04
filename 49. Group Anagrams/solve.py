class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for w in strs :
            res = "".join(sorted(w,key=ord))
            try:
                dic[res].append(w)
            except :
                dic[res] = [w]
        return dic.values()