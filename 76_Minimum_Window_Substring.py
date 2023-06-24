from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        occ_t = Counter(t)
        occ_c = Counter()
        l = 0
        min_window = ""

        for r in range(len(s)):
            occ_c[s[r]] += 1

            while all(occ_c[key] >= occ_t[key] for key in occ_t):
                current_window =  s[l:r + 1]
                current_window_length = r - l + 1
                if not min_window or current_window_length < len(min_window):
                    min_window = current_window
                occ_c[s[l]] -= 1
                l += 1

        return min_window
