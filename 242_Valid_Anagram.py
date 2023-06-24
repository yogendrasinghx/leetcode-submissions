class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)

        dic = {}

        if s_len != t_len:
            return False

        else:
            for char_s in s:
                if char_s in dic:
                    dic[char_s] += 1
                else:
                    dic[char_s] = 1

            for char_t in t:
                if char_t in dic:
                    dic[char_t] -= 1
                else:
                    return False
        print(dic)
        for value in dic.values():
            if value != 0:
                return False
            else:
                return True
sol  = Solution()
s = "aacc"
t ="ccac"

print(sol.isAnagram(s,t))