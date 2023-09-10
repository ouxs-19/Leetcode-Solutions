class Solution:
    def numberOfPoints(self, intervals: List[List[int]]) -> int:
                
        intervals.sort(key = lambda elem : elem[0])
        done = False

        while not done:
            done = True
            for i in range(1,len(intervals)):
                if intervals[i-1][1] >= intervals[i][0]:
                    intervals[i-1][1] = max(intervals[i][1], intervals[i-1][1])
                    del intervals[i]
                    done = False
                    break

        return sum(intervals[i][1]-intervals[i][0]+1 for i in range(len(intervals)))