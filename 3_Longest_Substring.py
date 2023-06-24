class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        p1 = 0
        p2 = 0
        max_string = 0

        occ = set()
        while p2 < n:
            if s[p2] not in occ:
                occ.add(s[p2])
                p2 += 1
                max_string = max(p2 - p1, max_string)
            else:
                occ.remove(s[p1])
                p1 += 1

        return max_string
