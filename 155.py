class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack)==0:
            self.minStack.append(val)
        elif (self.minStack[len(self.minStack)-1]>=val):
            self.minStack.append(val)

    def pop(self) -> None:
        removedNum = self.stack.pop()
        if (self.minStack[len(self.minStack)-1]==removedNum):
            self.minStack.pop()
        print(self.stack,self.minStack)
        
    def top(self) -> int:
        n = len(self.stack)
        return self.stack[n-1]

    def getMin(self) -> int:
        # return 0
        return self.minStack[len(self.minStack)-1]