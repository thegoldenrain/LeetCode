class MinStack:

    def __init__(self):
        self.li = []
        
        

    def push(self, x: int) -> None:
        (self.li).append(x)

    def pop(self) -> None:
        (self.li).pop()

    def top(self) -> int:
        return (self.li)[-1]

    def getMin(self) -> int:
        min = (self.li)[0]
        
        for i in self.li:
            if min > i:
                min = i
        return min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
