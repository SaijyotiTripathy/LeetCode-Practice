class FrontMiddleBackQueue:

    def __init__(self):
        self.l=[]

    def pushFront(self, val: int) -> None:
        self.l.insert(0,val)
        #print(self.l)

    def pushMiddle(self, val: int) -> None:
        n= len(self.l)
        self.l.insert(n//2,val)
        #print(self.l)

    def pushBack(self, val: int) -> None:
        self.l.append(val)
        #print(self.l)

    def popFront(self) -> int:
        if self.l==[]:
            return -1
        p= self.l[0]
        self.l.pop(0)
        #print(self.l)
        return p

    def popMiddle(self) -> int:
        if self.l==[]:
            return -1
        n= len(self.l)
        if n%2==0:
            p= self.l[(n//2)-1]
            self.l.pop(n//2-1)
        else:
            p= self.l[n//2]
            self.l.pop(n//2)
        #print(self.l)
        return p

    def popBack(self) -> int:
        if self.l==[]:
            return -1
        p= self.l[-1]
        self.l.pop()
        #print(self.l)
        return p


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()