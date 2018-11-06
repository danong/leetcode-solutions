class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == []:
            return 0
        shape = (len(grid), len(grid[0]))
        visited = [[False for _ in range(shape[1])] for _ in range(shape[0])]
        
        def neighbors(row, col):
            for offset in range(-1, 2, 2):
                new_row = row + offset
                new_col = col + offset
                if new_col >= 0 and new_col < shape[1]:
                    yield (row, new_col)
                if new_row >= 0 and new_row < shape[0]:
                    yield (new_row, col)
        
        def visit(row, col):
            visited[row][col] = True
            for n_row, n_col in neighbors(row, col):
                if grid[n_row][n_col] == '1' and not visited[n_row][n_col]:
                    visit(n_row, n_col)
                    
        islands = 0
        for row_idx, row in enumerate(grid):
            for col_idx, val in enumerate(row):
                if val == '1' and not visited[row_idx][col_idx]:
                    islands += 1
                    visit(row_idx, col_idx)
        return islands
