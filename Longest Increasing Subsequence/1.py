class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        trails = [nums[0]]
        
        for i in range(1, len(nums)):
            if nums[i] > trails[-1]:
                trails.append(nums[i])
            else:
                left, right = 0, len(trails) - 1
                # take use of binary search
                # it should find some spot in trail where nums[i] > trail[spot-1] but < trail[spot]
                # and set trail[spot] = nums[i]
                while left != right:
                    mid = (left+ right) / 2
                    if nums[i] > trails[mid] : 
                        left = mid + 1
                    elif nums[i] < trails[mid]:
                        right = mid
                    else:
                        break
                # it means that not exists trail[somewhere] = nums[i]
                if left == right:
                    trails[left] = nums[i]
        return len(trails)
                
                