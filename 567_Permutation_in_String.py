
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        count_s1 = Counter(s1)
        window = Counter(s2[:n1])

        if count_s1 == window:
            return True
        for i in range(n1,n2):
            window[s2[i]] += 1
            window[s2[i - n1]] -=1
            if window[s2[i - n1]] == 0:
                del window[s2[i - n1]]
            if count_s1 == window:
                return True

        return False



s1 = "ab"
s2 = "eidbaooo"
print(Solution().checkInclusion(s1,s2))