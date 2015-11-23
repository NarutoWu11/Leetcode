class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        
        # little improve from 2_2.py
        # use the relation between target and nums[left] to replace the recursion

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                if nums[mid] > nums[right]:
                    if target >= nums[left]:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < nums[right]:
                    right = mid - 1
                else:
                    right -= 1
            else:
                if nums[mid] > nums[right]:
                    left = mid + 1
                elif nums[mid] < nums[right]:
                    if target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    right -= 1
            
        if nums[left] == target:
            return True
        return False