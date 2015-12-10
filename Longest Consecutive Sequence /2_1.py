class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # convert list to set. takes O(n)

        nums = set(nums)
        
        best = 0
        
        # takes O(n) in the worst case
        for i in nums:
            if i - 1 not in nums:
                j = i + 1
                while j in nums:
                    j += 1
                best = max(best, j -i)
                
        
        return best