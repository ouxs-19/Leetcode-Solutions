class Solution(object):
    def isValidSerialization(self, preorder):
        preorder = preorder.split(",")
        count = 0 
        for elem in preorder  :
            if count < 0 :
                break
            if elem == "#" : count-=1
            else : count+=1
        else : 
            if count < 0 :
                return True 
        return False 