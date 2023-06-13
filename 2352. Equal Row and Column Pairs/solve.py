class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter = defaultdict(int)
        for row in grid :
            counter[tuple(row)] += 1 
        
        N = len(grid)
        cnt = 0

        for i in range(N):
            cnt += counter[tuple(grid[j][i] for j in range(N))]
        
        return cnt 