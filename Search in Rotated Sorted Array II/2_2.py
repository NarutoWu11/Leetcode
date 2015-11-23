class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        
        # different from 2_1.py. 
        # in another sight, first, compare the relation between nums[mid] and target; 
        # then, compare nums[mid] and nums[right]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                if nums[mid] > nums[right]:
                    return self.search(nums[:mid], target) or self.search(nums[mid+1:], target)
                    
                    
                elif nums[mid] < nums[right]:
                    right = mid - 1
                else:
                    right -= 1
            else:
                if nums[mid] > nums[right]:
                    left = mid + 1
                elif nums[mid] < nums[right]:
                    #right = mid - 1
                    return self.search(nums[:mid], target) or self.search(nums[mid+1:], target)
                    
                else:
                    right -= 1
            
        if nums[left] == target:
            return True
        return False