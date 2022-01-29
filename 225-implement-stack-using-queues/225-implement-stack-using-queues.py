class MyStack:

    def __init__(self):
        self.q1=[]
        self.q2=[]

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        if self.q1==[]:
            return -1
        
        while len(self.q1)!=1:
            self.q2.append(self.q1.pop(0))
            
        p= self.q1.pop(0)
        self.q1, self.q2= self.q2, self.q1
        return p

    def top(self) -> int:
        if self.q1==[]:
            return -1
        
        while len(self.q1)!=1:
            self.q2.append(self.q1.pop(0))
            
        p= self.q1[0]
        self.q2.append(self.q1.pop(0))
        self.q1, self.q2= self.q2, self.q1
        return p

    def empty(self) -> bool:
        if self.q1==[] and self.q2==[]:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()