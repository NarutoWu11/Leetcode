#import copy
#in-place
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        if not board or not board[0]:
            return 

        m, n = len(board), len(board[0])
        
        
        # [2nd bit, 1st bit] = [next state, current state]

        #- 00  dead (current) -> dead (next)
        #- 01  live (current) -> dead (next)
        #- 10  dead (current) -> live (next)
        #- 11  live (current) -> live (next)
        
        for i in xrange(m):
            for j in xrange(n):
                count = 0
                if i - 1 >= 0 and board[i-1][j] & 1 == 1:
                    count += 1
                if i - 1 >= 0 and j-1 >= 0 and board[i-1][j-1] & 1 == 1:
                    count += 1
                if i - 1 >= 0 and j + 1< n and board[i-1][j+1] & 1 == 1:
                    count += 1
                if j - 1 >= 0 and board[i][j-1] & 1 == 1:
                    count += 1
                if j + 1< n and board[i][j+1] & 1== 1:
                    count += 1
                if i + 1 < m and j-1 >= 0 and board[i+1][j-1] & 1 == 1:
                    count += 1
                if i + 1 < m and board[i+1][j] & 1 == 1:
                    count += 1
                if i + 1 < m and j + 1 < n and board[i+1][j+1] & 1 == 1:
                    count += 1
                
                # if next state is dead, we can leave the board unhandled, because in the next step, we let board >> 1, which
                # will let it be 0 in either way.
                
                #if count < 2:
                #    board[i-1][j-1] = 0
                #elif count > 3:
                #    board[i-1][j-1] = 0
                
                if count == 2 and board[i][j] == 1:
                    board[i][j] = 0b11
                elif count == 3:
                    board[i][j] |= 0b10
        
        for i in xrange(m):
            for j in xrange(n):
                board[i][j] >>= 1
        
                    
        