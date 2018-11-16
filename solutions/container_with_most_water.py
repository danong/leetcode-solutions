"""https://leetcode.com/problems/container-with-most-water/"""

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_volume = 0
        while left < right:
            cur_height = min(height[left], height[right])
            cur_vol = cur_height * (right - left)
            max_volume = max(max_volume, cur_vol)
            while left < right and height[left] <= cur_height:
                left += 1
            while right > left and height[right] <= cur_height:
                right -= 1
        return max_volume
