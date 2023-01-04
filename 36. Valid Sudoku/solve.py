import numpy as np
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(line):
            a = set()
            for char in line : 
                if char.isdecimal():
                    if char in a :
                        return True 
                    else :
                        a.add(char)
            return False 
            
        board = grid = np.array(board)
        for i in range(9):
            j, k = (i // 3) * 3, (i % 3) * 3
            if check(grid[i,:]) or  check(grid[:,i]) or check(grid[j:j+3, k:k+3].ravel()) : return False 
        return True 