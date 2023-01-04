from sortedcontainers import SortedDict as sd
class MyCalendarThree:

    def __init__(self):
        self.d = sd()

    def book(self, start: int, end: int) -> int:
        self.d[start] = self.d.get(start,0)+1
        self.d[end] = self.d.get(end,0)-1
        c, res = 0, 0
        for d in self.d.values():
            c+=d
            res = max(res,c)
        return res

