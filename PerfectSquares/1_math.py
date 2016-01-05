class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        return_1 = set()
        i = 1
        
        # if n == i*i, return 1
        # time complexity: O(n^(1/2))
        while i * i <= n:
            return_1.add(i*i)
            i += 1
        if n in return_1:
            return 1
        
        # if n in return_2, return 2
        # time complexity: O(n)
        return_2 = set()
        for i in return_1:
            for j in return_1:
                return_2.add(i+j)
        
        if n in return_2:
            return 2
        
        # O(n)
        for i in return_1:
            if n - i in return_2:
                return 3
        
        # Lagrange's four-square theorem
        return 4
        