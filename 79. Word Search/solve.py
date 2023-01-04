class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m, l = len(board) , len(board[0]), len(word)
        if len(word) == 0 : return False 
        def solve(i,j,lo):
            if l == lo : 
                return True 
            if i < 0 or j < 0 or i == n or j == m : return False
            if (i,j) not in watched and board[i][j] == word[lo] : 
                watched.append((i,j))
                if solve(i+1,j,lo+1) or  solve(i,j-1,lo+1) or  solve(i-1,j,lo+1) or  solve(i,j+1,lo+1) :
                    return True 
                watched.pop()
                
            return False 
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    watched = []
                    if solve(i,j,0) : return True 
        return False 