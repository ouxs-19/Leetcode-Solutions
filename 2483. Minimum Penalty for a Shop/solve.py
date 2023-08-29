class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        sm, best_sm, best_hour = 0, 0, 0 

        for hour, state in enumerate(customers):
            if state == "Y":
                sm -= 1
            else:
                sm += 1
            
            if sm < best_sm :
                best_sm = sm
                best_hour = hour + 1
        
        return best_hour

