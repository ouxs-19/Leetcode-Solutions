class MedianFinder:

    def __init__(self):
        self.index = -1
        self.mod = True
        self.nums = []

    def addNum(self, num: int) -> None:
        bisect.insort_left(self.nums,num)
        if self.mod :
            self.index += 1
        self.mod = not self.mod

    def findMedian(self) -> int:
        if self.mod : return (self.nums[self.index]+self.nums[self.index+1])/2
        return self.nums[self.index]