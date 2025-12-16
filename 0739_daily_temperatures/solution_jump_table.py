from typing import List 

# runtime: 56.80%, memory: 95.98% 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n: int = len(temperatures)
        answer: List[int] = [0] * n

        for i in range(n - 2, -1, -1):
            next_day: int = i + 1
            while next_day < n and temperatures[i] >= temperatures[next_day]:
                if answer[next_day] == 0:
                    break
                
                next_day += answer[next_day]
            
            if next_day < n and temperatures[i] < temperatures[next_day]:
                answer[i] = next_day - i
        
        return answer
            

        