from typing import List 

# runtime: 56.80%, memory: 87.39% 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer: List[int] = [0] * len(temperatures)
        stack: List[int] = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]: 
                answer[stack[-1]] = i - stack[-1]
                stack.pop()
            
            stack.append(i)
        
        return answer

        