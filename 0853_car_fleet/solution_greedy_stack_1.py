from typing import List, Tuple  

# runtime: 48.43%, memory: 33.10% 
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars: List[Tuple[int, int]] = sorted(zip(position, speed), reverse=True)
        fleets: int = 0
        times: List[int] = []  
        
        for pos, spd in cars:
            times.append(float(target - pos) / spd)
        
        stack: List[float] = []
        for i in range(len(position)):
            if not stack:
                fleets += 1
                stack.append(times[i])
            else:
                if times[i] > stack[-1]:
                    fleets += 1
                    stack.append(times[i])
            
        return fleets

        