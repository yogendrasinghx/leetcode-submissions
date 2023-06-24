#https://leetcode.com/problems/plus-one/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        new_num = []
        for digit in digits:
            num = num*10+digit

        num = num + 1

        while(num>0):
            new_num.append(num%10)
            num = num//10
        return new_num[::-1]