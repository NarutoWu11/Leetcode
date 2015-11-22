class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        def binarysearch(a, target):
            length = len(a)
            if length == 0:
                return False
            if a[length/2] == target:
                return True
            elif a[length/2] > target:
                b = a[0:length/2]
                return binarysearch(b, target)
            else:
                b = a[length/2+1:length]
                return binarysearch(b, target)
        newarray = []
        for i in range(len(matrix)):
            newarray.extend(matrix[i])
        return binarysearch(newarray, target)
                