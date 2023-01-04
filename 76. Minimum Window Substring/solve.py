class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n , m = len(s) , len(t)
        chars = Counter(t)
        goal , curr= len(chars) , 0 
        ptr_left , ptr_right = 0 , 0
        track = {}
        res = [float("-inf"),float("inf")]

        while ptr_right < n :
            c = s[ptr_right]
            track[c] = track.get(c, 0) +1 
            if c in chars and  track[c] == chars[c] :
                curr+=1
            while ptr_left <= ptr_right and curr == goal :
                c = s[ptr_left]
                if ptr_right-ptr_left+1 < res[1]-res[0]+1:
                    res = [ptr_left,ptr_right]
                track[c]-=1
                if c in chars and track[c]<chars[c]:
                    curr-=1
                ptr_left+=1
            ptr_right+=1
        if res[0]<0 :
            return ""
        return s[res[0]:res[1]+1]