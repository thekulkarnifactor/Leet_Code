# 36. Valid Sudoku
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows_map = defaultdict(set)
        cols_map = defaultdict(set)
        sub_box_map = defaultdict(set)

        for row in range(9):
            for col in range(9):
                digit = board[row][col]
                
                if digit == ".":
                    continue
                elif (digit in rows_map[row] or
                      digit in cols_map[col] or
                      digit in sub_box_map[(row // 3, col // 3)]):
                    return False
                else:
                    rows_map[row].add(digit)
                    cols_map[col].add(digit)
                    sub_box_map[(row // 3, col // 3)].add(digit)

        return True
        
