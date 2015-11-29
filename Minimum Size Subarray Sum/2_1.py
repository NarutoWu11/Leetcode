class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        left, right = 0, 0
        sumList = 0
        result = length + 1
        
        while right < length:
            sumList += nums[right]
            right += 1
            while sumList >= s:
                result = min(result, right - left)
                sumList -= nums[left]
                left += 1
        
        return 0 if result > length else result