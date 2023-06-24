#Problem Link : https://leetcode.com/problems/valid-palindrome/description/

# Approach 1 O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s= re.sub(r'[\W_]', '', s)
        return s[::-1] == s

# Approach 2 O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True