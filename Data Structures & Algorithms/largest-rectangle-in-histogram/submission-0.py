class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack= []
        area = 0


        for i in range(len(heights)):
            start = i
            while stack and heights[i] < stack[-1][1]:
                index, height = stack.pop()
                curr_area = height * (i - index) 
                area = max(area, curr_area)
                start = index

            stack.append((start, heights[i]))
        
        for index, height in stack:
            area = max(area, height * (len(heights) - index))
            
        return area



        