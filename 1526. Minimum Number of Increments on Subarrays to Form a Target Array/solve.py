class Solution(object):
        def minNumberOperations(self, target):
            if not target :
                return 0
            asend = True 
            decend = False 
            last = target[0]
            last_lowest = 0
            s = 0
            count = 0 
            for num in target:
                if asend :
                    if num < last :
                        count+=1
                        s+=last-last_lowest
                        asend = False 
                else :
                    if num > last : 
                        asend = True
                        last_lowest = last
                        
                last = num
            if asend :
                s+=num-last_lowest
            return s