from typing import Dict, List 

# runtime: 9.50%, memory: 17.72% 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d: Dict[int, bool] = {}
        for n in nums:
            if n in d.keys():
                return True
            d.update({n: False})
        return False
        
        