import sys
from typing import List 

# runtime: 23.73%, memory: 99.98%
class MinStack:
            

    def __init__(self):
        self._list: List = list()
        self._min: int = sys.maxsize
        self._top: int = -1
        

    def push(self, val: int) -> None:
        self._list.append(val)
        self._top += 1
        if val < self._min:
            self._min = val


    def pop(self) -> None:
        self._list.pop(self._top)
        self._top -= 1
        if self._top < 0:
            self._min = sys.maxsize
        else:
            self._min = min(self._list)
        

    def top(self) -> int:
        return self._list[self._top]
        

    def getMin(self) -> int:
        return self._min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()