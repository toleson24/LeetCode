import math 
from typing import List 

# 29 Jan 2025
# runtime: 9.07%, memory: 100.00% 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        oper_funcs = {
            "+": lambda x, y : x + y,
            "-": lambda x, y : x - y,
            "*": lambda x, y : x * y,
            "/": lambda x, y : math.trunc(x / y),
        }
        stack = []

        for t in tokens:
            if t in oper_funcs.keys():
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                t = f"{oper_funcs[t](op1, op2)}"

            stack.append(t)

        return int(stack.pop())

        