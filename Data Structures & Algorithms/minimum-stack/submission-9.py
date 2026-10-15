class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = float("inf")

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.minstack = val   
        else: 
            if val >= self.minstack:
                self.stack.append(val)
            else:
                self.stack.append(2*val - self.minstack)
                self.minstack = val
    def pop(self) -> None:
       
        mod = self.stack.pop()
        if mod < self.minstack:
            self.minstack = 2*self.minstack - mod

    def top(self) -> int:
        # return self.stack[-1]
        if self.stack[-1]<self.minstack:
            return self.minstack 
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack
        
