from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n
        i = 0
        while i < n:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                low = mid
            else:
                high = mid
            i += 1
        return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(Solution().search(nums, target))
