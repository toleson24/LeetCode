from typing import Dict, List 
from collections import defaultdict

# runtime: 83.04%, memory: 74.56% 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d: Dict[str, List[str]] = defaultdict(list)
        
        for s in strs:
            key: str = "".join(sorted(s))
            
            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]
            
        return [group for group in d.values()]


        