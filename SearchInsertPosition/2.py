class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        last_pos = 0
        while left <= right:
            middle = (left+right)/2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle -1
                last_pos = left
            else:
                left = middle+1
                last_pos = right
        return (middle + 1, middle )[last_pos == left]