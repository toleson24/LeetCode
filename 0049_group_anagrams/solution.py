class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # brute force: runtime: O(n^2)
        # strCopy = deepcopy(strs)
        # for i, s in enumerate(strCopy):         # O(n)
        #     strCopy.pop(i)
        #     s = ''.join(sorted(s))              # O(klogk)
        #     strCopy.insert(i, (i, s))
        
        # anagrams, skip = [], []
        # for i, s1 in strCopy:                   # O(n)
        #     if i in skip:                       # O(n) ? 
        #         continue
        #     newList = []
        #     newList.append(strs[i])
        #     for j, s2 in strCopy:               # O(n)
        #         if s1 == s2 and s1 is not s2:
        #             newList.append(strs[j])
        #             skip.append(j)
        #     anagrams.append(newList)

        # return anagrams

        groups = {}
        
        for word in strs:
            letters = ''.join(sorted(word))
            if letters in groups:
                groups[letters].append(word)
            else:
                groups[letters] = [word]

        return list(groups.values())  # list() necessary local, not on LeetCode


def main():
    solution = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(solution.groupAnagrams(strs))
    strs = [""]
    print(solution.groupAnagrams(strs))
    strs = ["a"]
    print(solution.groupAnagrams(strs))
    strs = ["","b"]
    print(solution.groupAnagrams(strs))


if __name__ == "__main__":
    main()
        
        