from collections import Counter

# runtime: 98.51%, memory: 62.79% 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars_s = Counter(s)
        chars_t = Counter(t)

        return chars_s == chars_t

        