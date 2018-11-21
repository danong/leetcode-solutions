from itertools import product

def get_outer(m, n):
    """
    Args:
        m (int): number of rows
        n (int): number of cols
    """
    for i in range(n):
        yield 0, i
        yield m - 1, i
    for i in range(1, m - 1):
        yield i, 0
        yield i, n - 1

        
def neighbors(row, col, m, n):
    for offset in range(-1, 2, 2):  # -1, +1
        if 0 <= row + offset < m:
            yield row + offset, col
        if 0 <= col + offset < n:
            yield row, col + offset


class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])    # m rows, n cols
        visit_queue = []
        for row, col in get_outer(m, n):
            if board[row][col] == 'O':
                visit_queue.append((row, col))
                
        while visit_queue:
            row, col = visit_queue.pop()
            if board[row][col] == 1:
                continue
            board[row][col] = 1
            for nrow, ncol in neighbors(row, col, m, n):
                if board[nrow][ncol] == 'O':
                    visit_queue.append((nrow, ncol))
        
        # set all O to X
        for row, col in product(range(m), range(n)):
            if board[row][col] == 'O':
                board[row][col] = 'X'
    
        # set all 1 to O
        for row, col in product(range(m), range(n)):
            if board[row][col] == 1:
                board[row][col] = 'O'
                    
                    
