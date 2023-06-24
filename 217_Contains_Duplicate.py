
# Approach 1

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = set(nums)
        return len(unique)< len(nums)

# Approach 2

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for elem in nums:
            if elem in dic:
                return True
            dic[elem] = 1
        return False