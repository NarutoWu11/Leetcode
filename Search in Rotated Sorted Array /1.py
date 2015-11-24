class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left+right)/2
            if nums[middle] == target:
                return middle
            else:
                if nums[middle] >= nums[left]:
                    if target >= nums[left] and target < nums[middle]:
                        right = middle-1
                    else:
                        left = middle+1
                else:
                    if target > nums[middle] and target <= nums[right]:
                        left = middle +1
                    else:
                        right = middle-1
        return -1