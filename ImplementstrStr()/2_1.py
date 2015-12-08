class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        haystack_len = len(haystack)
        needle_len = len(needle)
        
        if haystack_len == 0 and needle_len == 0:
            return 0
        
        if haystack_len < needle_len or haystack_len == 0:
            return -1
        
        
        
        difference = haystack_len - needle_len
        
        for i in range(0, difference+1):
            temp = haystack[i:i+needle_len]
            if temp == needle:
                return i
        return -1