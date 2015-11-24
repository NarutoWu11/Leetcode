class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        low, high = 0, len(nums)-1
        while low < high:
            middle = (low + high)/2
            if nums[middle]>= target:
                high = middle
            else:
                low = middle + 1
        # make sure nums[low] is the target. Then it must have the range.
        if nums[low] == target :
            low2, high2 = 0, len(nums)-1
            while low2<high2:
                middle2 = (low2 + high2)/2
                if nums[middle2]>= target+1:
                    high2 = middle2
                else:
                    low2 = middle2 + 1
            if target+1 <= nums[-1]:
                return [low, low2-1]
            #if target+1 is bigger than any value in nums, then it should return low to the end of nums.
            else:
                return [low, len(nums)-1]
        else:
            return [-1, -1]