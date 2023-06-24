# Problem Link : https://leetcode.com/problems/container-with-most-water/description/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            #Calculate Area
            length = right - left
            left_height = height[left]
            right_height = height[right]
            breath = min(left_height, right_height)
            area = length * breath

            #Store the Max Area
            if area > max_area:
                max_area = area

            #Check if left pipe height is smaller than right pipe height
            if left_height < right_height:
                left += 1
            # Check if right pipe height is smaller than left pipe height
            else:
                right -= 1

        return max_area