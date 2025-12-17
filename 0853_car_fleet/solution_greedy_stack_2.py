from typing import List, Tuple 

# runtime: 75.96%, memory: 30.13% 
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars: List[Tuple[int, int]] = sorted(zip(position, speed), reverse=True)
        fleets: int = 0

        times: List[int] = [float(target - pos) / s for pos, s in cars]
        
        stack: List[float] = []
        for time in times:
            if not stack or time > stack[-1]:
                fleets += 1
                stack.append(time)
            
        return fleets

        