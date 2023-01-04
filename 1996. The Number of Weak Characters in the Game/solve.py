class Solution:
    def numberOfWeakCharacters(self, p: List[List[int]]) -> int:
        p.sort(reverse=True)
        count = 0 
        last_x, max_y = 0, 0
        temp = 0 
        for c in p:
            if c[0] != last_x: max_y = temp
            if max_y > c[1]: count += 1
            temp = max(temp, c[1])
            last_x = c[0]
        return count