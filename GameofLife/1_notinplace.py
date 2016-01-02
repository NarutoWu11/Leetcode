#import copy
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        if not board or not board[0]:
            return 
    
        m, n = len(board), len(board[0])
        
        update_board = copy.deepcopy(board)
        
        for i in xrange(m):
            update_board[i].insert(0, 0)
            update_board[i].append(0)
        
        update_board.insert(0, [0] * len(update_board[0]))
        update_board.append([0] * len(update_board[0]))
        
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                count = 0
                if update_board[i-1][j] == 1:
                    count += 1
                if update_board[i-1][j-1] == 1:
                    count += 1
                if update_board[i-1][j+1] == 1:
                    count += 1
                if update_board[i][j-1] == 1:
                    count += 1
                if update_board[i][j+1] == 1:
                    count += 1
                if update_board[i+1][j-1] == 1:
                    count += 1
                if update_board[i+1][j] == 1:
                    count += 1
                if update_board[i+1][j+1] == 1:
                    count += 1
                if count < 2:
                    board[i-1][j-1] = 0
                elif count > 3:
                    board[i-1][j-1] = 0
                elif count == 3:
                    board[i-1][j-1] = 1
        
                    
        