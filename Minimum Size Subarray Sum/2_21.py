class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        def sizeCheck(s, nums, size):
            left, right = 0, 0
            sums = 0
            
            while right < len(nums):
                sums += nums[right]
                right += 1
                if right - left > size:
                    sums -= nums[left]
                    left += 1
                if sums >= s:
                    return True
            return False
        
        left, right = 0, len(nums)+1
        results = len(nums) + 1
        # in this way, results can reach len(nums) if left keeps adding one.
        while left < right:
            mid = (left + right) >> 1
            if sizeCheck(s, nums, mid):
                results = min(mid, results)
                right = mid
            else:
                left = mid + 1
        return 0 if results == len(nums) + 1 else results
        