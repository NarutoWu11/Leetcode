class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        left, right = 0, len(citations)
        length = len(citations)
    
        
        while left < right:
            mid = (left+right) >> 1
            if length - mid == citations[mid]:
                return length - mid
            if citations[mid] > length - mid:
                right = mid
            else:
                left = mid+1
                
                
            
        return length - right
        