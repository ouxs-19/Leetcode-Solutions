class Foo:
    def __init__(self):
        self.CalledFirst = False 
        self.CalledSecond = False 
        


    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.CalledFirst = True 

    def second(self, printSecond: 'Callable[[], None]') -> None:
        while not self.CalledFirst : 
            continue
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.CalledSecond = True

    def third(self, printThird: 'Callable[[], None]') -> None:
        while not self.CalledSecond : 
            continue
        # printThird() outputs "third". Do not change or remove this line.
        printThird()