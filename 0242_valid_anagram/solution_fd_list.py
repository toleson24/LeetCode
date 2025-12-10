from typing import List 

A_OFFSET: int = ord('a')

# runtime: 73:05, memory: 62.79%
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count: List[int] = [0] * 26
        
        for ch in s:
            count[ord(ch) - A_OFFSET] += 1

        for ch in t:
            if count[ord(ch) - A_OFFSET] == 0:
                return False
            count[ord(ch) - A_OFFSET] -= 1

        return True

        