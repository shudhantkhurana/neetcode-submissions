class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def analyse_small_square(board, i_start, i_end, j_start, j_end):
            square = set()
            for i in range(i_start, i_end):
                for j in range(j_start, j_end):
                    if board[i][j] == '.': continue
                    initial = len(square)
                    square.add(board[i][j])
                    if len(square) == initial:
                        return False
            return True

        # rows and cols
        for i in range(9):

            row_set = set()
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    if val in row_set: return False
                    row_set.add(val)

            col_set = set()
            for j in range(9):
                val = board[j][i]
                if val != '.':
                    if val in col_set: return False
                    col_set.add(val)

        return (analyse_small_square(board,0,3,0,3) and
                analyse_small_square(board,3,6,0,3) and        
                analyse_small_square(board,6,9,0,3) and
                analyse_small_square(board,0,3,3,6) and
                analyse_small_square(board,3,6,3,6) and
                analyse_small_square(board,6,9,3,6) and
                analyse_small_square(board,0,3,6,9) and
                analyse_small_square(board,3,6,6,9) and
                analyse_small_square(board,6,9,6,9))

