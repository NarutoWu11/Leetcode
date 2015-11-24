class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        left, right = 0, len(nums)- 1
        while left < right:
            mid = (left+ right ) >> 1
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        if nums[left] == target:
            target += 1
            left2, right2 = 0, len(nums)- 1
            while left2 < right2:
                mid = (left2+ right2 ) >> 1
                if nums[mid] >= target:
                    right2 = mid
                else:
                    left2 = mid + 1
            if nums[left2] == target-1:
                return [left, left2]
            else:
                return [left, left2-1]
        return [-1,-1]