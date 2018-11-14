"""https://leetcode.com/problems/spiral-matrix/"""

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        output = []
        row_begin = 0
        row_end = len(matrix) - 1
        col_begin = 0
        col_end = len(matrix[0]) - 1
        while row_begin <= row_end and col_begin <= col_end:  # todo
            # right
            for j in range(col_begin, col_end + 1):
                output.append(matrix[row_begin][j])
            row_begin += 1
            # down
            for i in range(row_begin, row_end + 1):
                output.append(matrix[i][col_end])
            col_end -= 1
            # left:
            if row_begin <= row_end:
                for j in range(col_end, col_begin - 1, -1):
                    output.append(matrix[row_end][j])
                row_end -= 1
            # up
            if col_begin <= col_end:
                for i in range(row_end, row_begin - 1, -1):
                    output.append(matrix[i][col_begin])
                col_begin += 1

        return output
