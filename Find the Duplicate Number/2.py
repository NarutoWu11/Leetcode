class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low_boundry, high_boundry = 1, len(nums)-1
        while low_boundry < high_boundry:
            mid = low_boundry + (high_boundry - low_boundry)/2
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1
            # note that we cannot code as "count == mid", since 
            # we may get multiple duplication of n which is bigger 
            # than mid.

            # so for i <= mid, the maximum number that stays normal 
            # is mid
            if count <= mid:
                low_boundry = mid + 1
            else:
                high_boundry = mid
            
            
        return low_boundry