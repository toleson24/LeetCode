from typing import List 

# runtime: 98.56%, memory: 99.50% 
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars: List[int] = sorted(range(len(position)), key=lambda i: position[i], reverse=True)
        
        fleets: int = 0
        prev: float = 0.0

        for car in cars:
            time: float = float(target - position[car]) / speed[car] 
            if time > prev:
                fleets += 1
                prev = time
            
        return fleets

        