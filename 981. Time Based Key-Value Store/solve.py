from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.tp = defaultdict(SortedDict)        
        self.start = defaultdict(lambda :float("inf"))
        self.times = defaultdict(bool)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tp[key][timestamp] = value
        self.start[key] = min(self.start[key],timestamp)
        self.times[timestamp] = True
            
    def get(self, key: str, timestamp: int) -> str:
        if timestamp<self.start[key]:
            return ""
        vals = self.tp[key].values()
        ind = self.tp[key].bisect_left(timestamp)
        if self.times[timestamp] : 
            return vals[ind]
        return vals[ind-1]
            
            
