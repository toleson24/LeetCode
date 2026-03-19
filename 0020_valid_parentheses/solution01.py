from collections import deque 

# runtime: 100.00%, memory: 57.01%
class Solution:
    def isValid(self, s: str) -> bool: 
        parens = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        stack = deque()

        for ch in s:
            if stack and ch in parens:
                if stack[-1] == parens[ch]:
                    stack.pop()
                else:
                    stack.append(ch)
            else: 
                stack.append(ch)

        return len(stack) == 0 

        