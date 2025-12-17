from typing import List 

# runtime: 84.45%, memory: 99.09% 
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        prev = float("-inf")

        for p, s in cars:
            time = (target - p) / s
            if time > prev:
                fleets += 1
                prev = time

        return fleets
        
        