#Problem Link : https://leetcode.com/problems/perfect-number/submissions/959574965/
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        s = 1
        for i in range(2,math.floor(math.sqrt(num))+1):
            if num % i == 0:
                s = s + i + num/i
        if s == num:
            return True
        else:
            return False