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
            if length - mid - 1 >= citations[mid]:
                # mid == length - 1, in this situation, mid is the largest index of citations, left = right - 1 = legnth - 2
                if mid == length - 1 or citations[mid+1] > length - mid - 2:
                    return length - mid - 1
                else:
                    left = mid
            else:
                right = mid
                
                
            
        return length - right