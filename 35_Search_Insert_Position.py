#Problem Link : https://leetcode.com/problems/search-insert-position/description/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        elif target > nums[-1]:
            return len(nums)
        else:
            i = 0
            for num in nums:
                if target > num:
                    i = i + 1
                else:
                    return i