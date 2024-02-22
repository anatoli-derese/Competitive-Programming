class MinStack:
    def __init__(self):
        self.minStack = []
        self.stack  =[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0 or self.minStack[-1] >= val:
            self.minStack.append(val)


    def pop(self) -> None:
        val = self.stack.pop()
        if self.minStack and self.minStack[-1] == val:
            self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]


# Your self.minStack object will be instantiated and called as such:
# obj = self.minStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()