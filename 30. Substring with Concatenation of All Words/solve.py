class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        l = len(words[0])
        need = len(words)*l
        words = Counter(words)
        backup = words.copy()
        idx = []
        i = 0 
        m = len(s)
        h = m-l+1
        while i < h :
            if words[s[i:i+l]] :
                words[s[i:i+l]]-=1
                start = i 
                i+=l
                while i-start != need and i < h : 
                    if words[s[i:i+l]]: 
                        words[s[i:i+l]]-=1
                        i+=l
                    else : 
                        break 
                if i-start == need : 
                    idx.append(start)
                words = backup.copy()
                i = start
            i+=1
        return idx