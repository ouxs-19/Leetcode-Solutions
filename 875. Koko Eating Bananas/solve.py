from math import ceil

class Solution:
    def minEatingSpeed(self, pile: List[int], h: int) -> int:
        inf = 1
        sup = max(pile)
        while inf <= sup :
            mid = (inf + sup) // 2
            if sum(ceil(bananas / mid) for bananas in pile) > h:
                inf = mid + 1
            else:
                sup = mid - 1
        return inf