#Problem Link : https://leetcode.com/problems/longest-consecutive-sequence/description/

# Approach 1 : O(nlogn)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums = sorted(nums)

        print(nums)
        counter = 1
        counter_list = []
        n = len(nums)
        if n == 0:
            return 0
        for i, num in enumerate(nums):

            if i < n - 1 and nums[i + 1] == num + 1:
                counter += 1
            else:
                counter_list.append(counter)
                counter = 1
        return max(counter_list)

# Approach 1 : O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        counter = 1
        counter_list = []
        n = len(nums)
        if n == 0:
            return 0
        for num in nums:
            if num - 1 not in nums:
                counter = 1
                current_num = num

                while current_num + 1 in nums:
                    counter += 1
                    current_num += 1

            counter_list.append(counter)

        return max(counter_list)