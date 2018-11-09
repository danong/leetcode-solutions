"""https://leetcode.com/problems/sudoku-solver/"""


class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.solve()

    def solve(self):
        row, col = self.first_empty_cell()
        if row == col == -1:
            return True
        for i in '123456789':
            if self.is_valid(row, col, i):
                self.board[row][col] = i
                if self.solve():
                    return True
                self.board[row][col] = '.'
        return False

    def first_empty_cell(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '.':
                    return row, col
        return -1, -1

    def is_valid(self, row, col, i):
        return all((self.is_valid_row(row, i), self.is_valid_col(col, i),
                    self.is_valid_subboard(row, col, i)))

    def is_valid_row(self, row, i):
        for col in range(9):
            if self.board[row][col] == i:
                return False
        return True

    def is_valid_col(self, col, i):
        for row in range(9):
            if self.board[row][col] == i:
                return False
        return True

    def is_valid_subboard(self, row, col, i):
        row -= row % 3
        col -= col % 3
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                if self.board == i:
                    return False
        return True
