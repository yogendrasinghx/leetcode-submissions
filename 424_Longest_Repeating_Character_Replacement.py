class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        occ = {}

        p1 = 0
        p2 = 0
        maxSubString = 0
        maxCount = 0

        while p2 < n:
            char = s[p2]
            occ[char] = occ.get(char, 0) + 1
            maxCount = max(maxCount, occ[char])

            if p2 - p1 + 1 - maxCount > k:
                occ[s[p1]] -= 1
                p1 += 1
            maxSubString = max(maxSubString, p2 - p1 + 1)
            p2 += 1

        return maxSubString


s = "ABAB"
k = 2
print(Solution().characterReplacement(s,k))