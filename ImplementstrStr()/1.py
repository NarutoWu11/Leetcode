class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        len_haystack = len(haystack)
        len_needle = len(needle)
        if len_needle == 0:
            return 0
        minus = len_haystack - len_needle
        for i in range(0, minus+1):
            if haystack[i:i+len_needle] == needle:
                return i
        return -1