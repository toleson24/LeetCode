# runtime: 88.59%, memory: 31.53%
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False

        s = s.lower()
        s = ''.join([ch for ch in s if ch.isalnum()])

        l: int = len(s)
        i: int = 0
        j: int = l - 1

        while i <= j:
            if s[i] != s[j]:
                return False

            i += 1
            j -= 1
        
        return True

        