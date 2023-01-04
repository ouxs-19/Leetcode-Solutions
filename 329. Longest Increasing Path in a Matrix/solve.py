class Node:
    def __init__(self, id, val):
        self.id  = id
        self.val = val
        self.sons = []

    def add_son(self, n):
        self.sons.append(n)

class Solution:
    def longestIncreasingPath(self, arr: List[List[int]]) -> int:
        
        def solve(node, n):
            r = 0
            for child in node.sons:
                if dp[child.id] == 0:
                    r = max(solve(child, 0), r)
                else:
                    r = max(dp[child.id], r)


            dp[node.id] = n + r + 1

            return dp[node.id]
        
        dxs = [0, 0, 1, -1]
        dys = [-1, 1, 0, 0]

        H, W = len(arr), len(arr[0])

        new_arr = [[0]*W for _ in range(H)]

        for i in range(H):
            for j in range(W):
                new_arr[i][j] = Node(i*W+j, arr[i][j])
                
                
        for i in range(H):
            for j in range(W):
                # print(i, j)
                for dx, dy in zip(dxs, dys):
                    if (0<=i+dx<H) and (0<=j+dy<W) and (new_arr[i+dx][j+dy].val > new_arr[i][j].val):
                        new_arr[i][j].add_son(new_arr[i+dx][j+dy])

                        
        dp = [0] * W * H
        for i in range(H):
            for j in range(W):
                if not dp[new_arr[i][j].id]:
                    solve(new_arr[i][j], 0)
                    
        return max(dp)