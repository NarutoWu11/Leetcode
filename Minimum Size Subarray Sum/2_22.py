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
        
        left, right = 0, len(nums)
        results = len(nums) + 1

        # right originally is len(nums), so if we want results to be ablt to equal to len(nums),
        # then should be left <= right
        while left <= right:
            mid = (left + right) >> 1
            if sizeCheck(s, nums, mid):
                results = min(mid, results)

                # we cannot write "right = mid" like 2_21.py, since when left = right, it will keep in the loop forever.
                right = mid - 1
            else:
                left = mid + 1
        return 0 if results == len(nums) + 1 else results
        