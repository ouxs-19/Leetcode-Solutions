class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        def merge(intervals):
            ans = []
            for beg, end in sorted(intervals):
                if not ans or ans[-1][1] < beg:
                    ans += [[beg, end]]
                else:
                    ans[-1][1] = max(ans[-1][1], end)
            return sum(j-i for i,j in ans)
        sides_lft = [(x1,0,y1,y2) for x1,y1,x2,y2 in rectangles]
        sides_rgh = [(x2,1,y1,y2) for x1,y1,x2,y2 in rectangles]
        sides = sorted(sides_lft + sides_rgh)
        intervals, ans, prev_x = [], 0, sides[0][0]
        for x, op_cl, y1, y2 in sides:
            ans+=merge(intervals) * (x - prev_x)
            if op_cl == 0:
                intervals.append((y1,y2))
            else:
                intervals.remove((y1,y2))     
            prev_x = x
        return ans % (10**9 + 7)