class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda elem : elem[0], reverse = True)
        new_intervals = [intervals[0]]
        
        for a, b in intervals[1:]:
            if new_intervals[-1][0] >= b: 
                new_intervals.append([a, b])
        
        return len(intervals)-len(new_intervals)