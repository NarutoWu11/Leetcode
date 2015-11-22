class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        numbers = []
        for i in range(len(matrix)):
            numbers += matrix[i]
        if not numbers:
            return False
        else:
            left , right = 0, len(numbers)-1
            while left < right:
                mid = (left + right ) >> 1
                if numbers[mid] > target:
                    right = mid - 1
                elif numbers[mid] < target:
                    left = mid + 1
                else:
                    return True
            if numbers[left] == target:
                return True
            else:
                return False