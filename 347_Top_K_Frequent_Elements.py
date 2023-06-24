
# Approach 1
"""
Create a Dictionary of Occurrence/Frequency of element then sort the dictionary
by value in decreasing order. And Final print the value up to k elements
Time Complexity = O(nlogn)
"""
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = {}
        result = []
        for num in nums:
            if num in occ:
                occ[num] += 1
            else:
                occ[num] = 1
        frequency = sorted(occ.items() ,key=lambda x :x[1] ,reverse=True)
        print(frequency)
        for i in range(k):
            result.append(frequency[i][0])

        return result


# Approach 2
'''
Create a Dictionary of Occurrence/Frequency of element. If the length of the ans list is less than k,
it means there is still space to add elements. In this case, it uses heapq.heappush() to add the pair [val, key]
(frequency, number) to the ans list as a min-heap. The min-heap ensures that the elements with the lowest frequency
are at the top.If the length of ans is already equal to k, it means the list is full. In this case, it uses 
heapq.heappushpop() to simultaneously push the current pair and pop the smallest element from the min-heap ans.
This ensures that only the k most frequent elements are kept in the ans list. And Finally print the value up to 
k elements
Time Complexity = O(klogn)
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        freq = dict()

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        for key, val in freq.items():
            if len(ans) < k:
                heapq.heappush(ans, [val, key])
            else:
                heapq.heappushpop(ans, [val, key])

        return [key for value, key in ans]

nums = [1, 2]
k = 2
sol = Solution1()
print(sol.topKFrequent(nums, k))

