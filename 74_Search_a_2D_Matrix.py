from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        low = 0
        high = n
        i = 0
        while i < n:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            elif target > nums[mid]:
                low = mid
            else:
                high = mid
            i += 1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n = len(matrix)
        low = 0
        high = n
        i = 0

        while i < n:
            mid = (low + high) // 2
            print(mid)
            if target > matrix[mid][-1]:
                low = mid
            elif target < matrix[mid][0]:
                high = mid
            else:
                return self.search(matrix[mid],target)
            i += 1

        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 30
print(Solution().searchMatrix(matrix, target))