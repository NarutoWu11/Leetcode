class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        # time complexity is O(nlogn)
        
        distance = len(nums)+1
        sums = [0,]
        # O(n)
        for i in range(len(nums)):
            sums.append(sums[i]+nums[i])
        #sums.remove(0)
        for i in range(len(sums)):
            if sums[i] >= s:
                binary_search_target = sums[i]- s
                start, end = 0, i-1
                mid = (start+end)/2
                while not(sums[mid]<= binary_search_target and sums[mid+1]>binary_search_target):
                    if sums[mid] < binary_search_target and sums[mid+1] <= binary_search_target:
                        start = mid + 1
                        mid = (start+end)/2
                    elif sums[mid]>binary_search_target:
                        end = mid-1
                        mid = (start+end)/2
                distance = min(distance, i-mid)
        return [0, distance][distance <= len(nums)]
                        
                    