class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        length = len(citations)
        if not length:
            return 0
        
        left, right = 0, length-1
        
        while left < right:
            mid = (left+ right) >> 1
            if length - mid == citations[mid]:
                return citations[mid]
            if length - mid > citations[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return (length - left, length - left - 1 )[ length - left> citations[left] ]