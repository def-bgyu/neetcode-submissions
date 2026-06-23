class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)- 1

        max_water = 0
        while left < right:
            width = right - left
            area = min(heights[right], heights[left]) * width
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
            max_water = max(area,max_water)

        return max_water
        