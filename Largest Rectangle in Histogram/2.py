class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        def length(height_a):
            res = [0] * len(height_a)
            stack = []
            for i in range(len(height_a)):
                while len(stack) and height_a[stack[-1]] > height_a[i]:
                    top = stack.pop()
                    res[top] = i - top - 1
                stack.append(i)
            for i in stack:
                res[i] = len(height_a) - i- 1
            return res
        
        res_right = length(height)
        res_left = length(height[::-1])[::-1]
        
        max_num = 0
        for i in range(len(height)):
            max_num = max(max_num, (res_right[i] + res_left[i] + 1) * height[i])
        return max_num