class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        s = lambda n : abs(n-x)
        arr.sort(key=s)
        return sorted(arr[:k])
        