class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row_0 = col_0 = False
        # step 1: iterate through matrix and set 0 markers in 1st row and col (except top left)
        for row_idx, row in enumerate(matrix):
            for col_idx, val in enumerate(row):
                if val == 0:
                    # set 0 marker
                    if col_idx == 0:
                        col_0 = True
                    else:
                        matrix[0][col_idx] = 0
                    if row_idx == 0:
                        row_0 = True
                    else:
                        matrix[row_idx][0] = 0

        # step 2: iterate through 1st row and col and propogate 0s (except top left)
        for idx, val in enumerate(matrix[0]):
            if idx == 0:
                continue
            if val == 0:
                # propogate 0s down
                for row in matrix[1:]:
                    row[idx] = 0
        for idx, row in enumerate(matrix):
            if idx == 0:
                continue
            if row[0] == 0:
                matrix[idx] = [0 for _ in range(len(row))]

        # step 3: propogate top left
        if row_0:
            matrix[0] = [0 for _ in range(len(matrix[0]))]
        if col_0:
            for row in matrix:
                row[0] = 0
