class MyCircularQueue:

    def __init__(self, k: int):
        self.q = []
        self.max = k
        self.cnt = 0

    def enQueue(self, value: int) -> bool:
        if self.cnt == self.max : 
            return False
        self.q.append(value)
        self.cnt += 1
        return True
    def deQueue(self) -> bool:
        if self.cnt == 0 : 
            return False
        self.q.pop(0)
        self.cnt -=1
        return True

    def Front(self) -> int:
        if self.cnt > 0 :
            return self.q[0]
        return -1

    def Rear(self) -> int:
        if self.cnt > 0 :
            return self.q[-1]
        return -1

    def isEmpty(self) -> bool:
        return self.cnt == 0 

    def isFull(self) -> bool:
        
        return self.cnt == self.max


