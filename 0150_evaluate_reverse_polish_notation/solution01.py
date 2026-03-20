import math 
from typing import List 

# 28 Jan 2025
# runtime: 57.15%, memory: 100.00% 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: List[str] = []
        oper_funcs = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: math.trunc(x / y)
        }
        
        for token in tokens:
            if token in oper_funcs.keys():
                op2 = int(stack.pop())
                op1 = int(stack.pop())

                token = oper_funcs[token](op1, op2)
                
            stack.append(f"{token}")
            
        return int(stack.pop())
        
        