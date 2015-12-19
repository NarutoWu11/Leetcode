# another brutal force
# simplify the while loop
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = j = 0
        while True:
            j = 0
            while True:
                if j == len(needle):
                    return i
                if j + i == len(haystack):
                    return -1
                if haystack[i + j] != needle[j]:
                    break
                j += 1
            
            i += 1