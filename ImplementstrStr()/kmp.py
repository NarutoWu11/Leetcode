class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_haystack = len(haystack)
        len_needle = len(needle)
        if len_needle == 0:
            return 0
        elif len_haystack < len_needle:
            return -1
        
        lps = self.initLPS(needle)
        i, j = 0, 0
        
        while j < len_haystack:
            if needle[i] == haystack[j]:
                if i == len_needle-1:
                    return j - i
                i += 1
                j += 1
                
                
            # needle[i] != haystack[j]    
            else:
                if i == 0:
                    j += 1
                # i > 0
                else:
                    i = lps[i-1]
        
        return -1
        
    
    def initLPS(self, needle):
        length = 0
        i = 1
        lps = [0, ]
        
        while i < len(needle):
            if needle[i] == needle[length]:
                length += 1
                lps.append(length)
                i += 1
                
            #needle[i] != needle[length]
            else:
                if length != 0:
                    length = lps[length - 1]
                #length == 0
                else:
                    length = 0
                    lps.append(length)
                    i += 1
                    
        return lps