from typing import Set

# runtime: 6.76%, memory: 52.70%
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _set: Set[str] = set()
        max_len: int = 0

        end: int = 0
        for beg in range(len(s)):
            _set.add(s[beg])

            end = beg + 1
            while end < len(s) and s[end] not in _set:
                _set.add(s[end])
                end += 1
            
            max_len = max(max_len, (end - beg))
            _set = set()

        return max_len

        