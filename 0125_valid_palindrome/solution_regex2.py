import re
from typing import List

# runtime: 85.90%, memory: 23.57%
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        if not s:
            return True
        
        l: int = 0
        r: int = len(s) - 1
        while l < r and s[l] == s[r]:
            l += 1
            r -= 1

        return s[l] == s[r]

        