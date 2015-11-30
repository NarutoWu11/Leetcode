# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = n + 1
        left, right = 1, n
        while left <= right:
            mid = (left + right) >> 1
            if isBadVersion(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result