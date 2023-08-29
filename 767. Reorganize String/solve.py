class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        if c.most_common()[0][1] > math.ceil(len(s)/2):
            return ""
        
        chars = []
        rearr_s = ""

        for char, occur in c.most_common():
            heapq.heappush(chars, (-occur, char) )
        
        while len(chars) > 1 :

            elem1 = heapq.heappop(chars)
            elem2 = heapq.heappop(chars)

            rearr_s += (elem1[1] + elem2[1])

            if elem1[0] < -1 : heapq.heappush(chars, (elem1[0]+1,elem1[1]) )
            if elem2[0] < -1 : heapq.heappush(chars, (elem2[0]+1,elem2[1]) )

        if len(chars) == 1 :
            elem = heapq.heappop(chars)
            rearr_s += elem[1]

        return rearr_s
