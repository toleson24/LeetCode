from typing import Optional  

# runtime: 83.22%, memory: 6.74%
class Node:
    def __init__(self, val: int, curr_min: int):
        self.data: int = val
        self.next: Optional[Node] = None
        self.min: int = curr_min

class MinStack:

    def __init__(self):
        self._top: Optional[Node] = None
        self.length: int = 0
        

    def push(self, val: int) -> None:
        if self._top is None:
            node: Optional[Node] = Node(val, val)
        else:
            node: Optional[Node] = Node(val, min(val, self._top.min))
            node.next = self._top
        
        self._top = node
        self.length += 1
        

    def pop(self) -> None:
        if not self._top:
            return
        
        self._top = self._top.next 
        self.length -= 1
        

    def top(self) -> int:
        return self._top.data
        

    def getMin(self) -> int:
        return self._top.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()