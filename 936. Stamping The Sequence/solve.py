class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        
        def check(ind):
            for j in range(window):
                if not (target[j+ind] == '?' or target[j+ind] == stamp[j]):
                    return False 
            return True
        
        window, l = len(stamp), len(target)
        past_splits = set()
        target = [char for char in target]
        res = []
        
        for i in range(l-window+1):
            if check(i):
                for j in range(i, -1, -1 ):
                    if j in past_splits:
                        break
                    past_splits.add(j)
                    if check(j):
                        res.append(j)
                        target[j:j+window] = ['?'] * window
        if all(char == '?' for char in target) : 
            return res[::-1]
        return []
                        
                    