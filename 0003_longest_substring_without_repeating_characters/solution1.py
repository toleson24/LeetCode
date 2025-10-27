from typing import Set

# runtime: 5.01%, memory: 52.70%
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        chars = set()
        end: int = 0
        longest: int = 0
        length: int = len(s)
        
        for beg in range(length):
            end = beg
            while end < length and s[end] not in chars:
                chars.add(s[end])
                longest = max(longest, (end - beg) + 1)
                end += 1
            chars = set()

        return longest
        