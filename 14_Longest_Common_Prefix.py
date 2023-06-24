class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        smallest = len(strs[0])
        for word in strs:
            if (len(word) < smallest):
                smallest = len(word)
        fword = strs[0]
        for i in range(smallest):
            flag = False
            for word in strs:
                if word[i]==fword[i]:
                    flag = True
                else:
                    return prefix
            if (flag):
                prefix = prefix + word[i]
        return prefix