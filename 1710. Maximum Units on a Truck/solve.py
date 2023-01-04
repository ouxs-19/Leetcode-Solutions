class Solution(object):
    def maximumUnits(self, b, t):
        b.sort(key=lambda box: box[1], reverse=True)
        s =  0
        for box in b : 
            if box[0] < t :
                s+=box[0]*box[1]
                t-=box[0]
            else :
                s+=box[1]*t
                break
        return s 