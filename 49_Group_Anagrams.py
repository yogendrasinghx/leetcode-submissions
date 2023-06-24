from typing import List


# Approach 1
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for word in strs:
            k = ''.join(sorted(word))
            if k not in dic:
                dic[k] = [word]
            else:
                dic[k].append(word)

        return list(dic.values())

# Approach 2



sol = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(sol.groupAnagrams(strs))