from typing import List 

# runtime: 51.34%, memory: 76.62% 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer: List[int] = [0 for _ in range(len(temperatures))]
        stack: List[int] = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]: 
                answer[stack[-1]] = i - stack[-1]
                stack.pop()
            
            stack.append(i)
        
        return answer

        