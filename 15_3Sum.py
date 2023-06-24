# Approach 1 O(n*n)
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dict = {}
        n = len(nums)
        triplets = set()
        result = []
        for i,num in enumerate(nums):
            dict[num] = i

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
            for j in range(i+1,n-1):
                complement = 0 - (nums[i] + nums[j])
                if complement in dict and dict[complement] !=i and dict[complement] !=j:
                    triplets.add((nums[i],nums[j],complement))
                    #result.append([nums[i],nums[j],complement])
        return triplets



nums = [-1,0,1,2,-1,-4]

print(Solution().threeSum(nums))