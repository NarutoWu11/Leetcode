class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right) >> 1
            
            # normal return situation
            if mid + 1 <= len(nums) and mid - 1 >= 0 and nums[mid-1] < nums[mid] > nums[mid + 1]:
                return mid
            
            # boundry situation
            if mid == 0:
                if nums[mid + 1] < nums[mid]:
                    return mid
                else:
                    return mid + 1
            
            # if mid == len(nums) - 1 is a situation we don't need to consider
            # since if it exists, then must be left = right = len(nums)-1. It won't appear in this loop.
            
            # normal situation, not return, binary search
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1

        return left