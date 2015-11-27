# time complexity is O(n)
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        start, end = 0, 0
        results = len(nums)+1
        sums = 0
        
        while end < len(nums):
            while sums < s and end < len(nums):
                sums += nums[end]
                end += 1
            while sums >= s and start < end:
                results = min(results, end-start)
                sums -= nums[start]
                start += 1
        return (0, results)[results <= len(nums)]