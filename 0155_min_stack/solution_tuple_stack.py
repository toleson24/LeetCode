from typing import List, Tuple 

# runtime: 83.22%, memory: 25.73% 
class MinStack:

    def __init__(self):
        self.stack: List[Tuple[int, int]] = []
        

    def push(self, val: int) -> None:
        curr_min: int = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, curr_min))
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()