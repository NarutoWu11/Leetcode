class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if nums[mid] >= nums[right]:
                    if target >= nums[left]:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < nums[right]:
                    right = mid - 1
            else:
                if nums[mid] >= nums[right]:
                    left = mid + 1
                elif nums[mid] < nums[right]:
                    if target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
            
        if nums[left] == target:
            return left
        return -1