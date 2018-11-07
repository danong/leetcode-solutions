from collections import deque


class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        max_rows = len(matrix)
        max_cols = len(matrix[0])
        
        bfs = deque([])
        
        for row in range(max_rows):
            for col in range(max_cols):
                if matrix[row][col] == 0:
                    bfs.append((row, col))
                else:
                    matrix[row][col] = float('inf')
                    
        neighbors = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
        while bfs:
            row, col = bfs.popleft()
            for n in neighbors:
                nrow = row + n[0]
                ncol = col + n[1]
                if 0 <= nrow < max_rows:
                    if 0 <= ncol < max_cols:
                        if matrix[nrow][ncol] > matrix[row][col] + 1:
                            matrix[nrow][ncol] = matrix[row][col] + 1
                            bfs.append((nrow, ncol))
        return matrix
