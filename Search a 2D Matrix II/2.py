class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # O(m + n)

        if not matrix:
            return False
        else:
            i, j = len(matrix) - 1, 0
            while i > -1 and j < len(matrix[0]):
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] > target:
                    i -= 1
                else:
                    j += 1
            return False