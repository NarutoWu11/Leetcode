class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        right = self.process(height)
        left = self.process(height[::-1])[::-1]
        
        maxArea = 0
        
        for i in range(len(height)):
            maxArea = max(maxArea, height[i] * (1+right[i] + left[i])) 
        return maxArea
        
    def process(self, height):
        width = [0, ] * len(height)
        stack = []
        
        for i in range(len(height)):
            while len(stack) > 0 and height[stack[-1]] > height[i]:
                temp = stack.pop()
                width[temp] = i - temp - 1
            
            
            stack.append(i)
            
        for i in stack:
            width[i] = len(height)- 1 - i
        
        return width