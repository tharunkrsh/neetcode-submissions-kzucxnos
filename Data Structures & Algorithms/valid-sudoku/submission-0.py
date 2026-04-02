class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set) # key = col. index
                                            # val = set of each col.
        rows = collections.defaultdict(set)  # key = row index
                                            # val = set of each row
        squares = collections.defaultdict(set) # key = (r/3, c/3 
                                               # val = set of each square


        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue 
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)] ):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c// 3)].add(board[r][c])

            
        return True
        