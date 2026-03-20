import math 
from typing import List

# runtime: 57.15%, memory: 88.48% 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            '+': lambda x, y : x + y, 
            '-': lambda x, y : x - y, 
            '*': lambda x, y : x * y, 
            '/': lambda x, y : math.trunc(x / y)
        }
        stack = []

        for tok in tokens: 
            if tok in operations:
                y = stack.pop() 
                tok = operations[tok](stack.pop(), y) 
            
            stack.append(int(tok))

        return stack.pop()

        