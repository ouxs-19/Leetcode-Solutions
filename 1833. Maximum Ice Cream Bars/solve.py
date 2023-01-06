class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        buy = 0
        for cost in costs :
            if cost > coins :
                break
            buy += 1
            coins -= cost
        return buy 