class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon or not dungeon[0]:
            return 1
        
        x, y = len(dungeon), len(dungeon[0])
        
        # hp[i][j] is the health point the knight has when he passes dungeon[i][j]
        hp = [[0] * y for i in range(x)]
        
        # decide the value of hp[x-1][y-1]
        if dungeon[x - 1][y - 1] < 0:
            hp[x - 1][y - 1] = 1
        else:
            hp[x - 1][y - 1] = dungeon[x- 1][y - 1] + 1
        
        # decide the value of the rightest col and the lowest row 
        for i in range(y-2, -1, -1):
            hp[x - 1][i] = max(1, hp[x - 1][i + 1] - dungeon[x - 1][ i + 1])
        
        for i in range(x -2, -1, -1):
            hp[i][y - 1] = max(1, hp[i + 1][y - 1] - dungeon[i + 1][y - 1])
            
        # decide the value of other hp 
        for i in range(x - 2, -1, -1):
            for j in range(y - 2, -1, -1):
                right = max(1, hp[i][j + 1] - dungeon[i][ j + 1])
                down = max(1, hp[i + 1][j] - dungeon[i + 1][j])
                
                hp[i][j] = min(right, down)
        
        return max(hp[0][0] - dungeon[0][0], 1)