class Solution:
    def check_row(self, lst):
        s = ''.join(lst)
        for i in '123456789':
            if s.count(i)>1:
                return True
        return False

    def check_triple(self,board):
        for i in range(3):
            for j in range(3):
                r = []
                for col in range(3):               
                    for row in range(3):
                        r.append(board[i*3 + col][j*3 + row])
                if self.check_row(r):
                    return True
        return False



    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board90 = [list(reversed(col)) for col in zip(*board)]

        for i in range(9):
            if self.check_row(board90[i]):
                return False
            if self.check_row(board[i]):
                return False
        if self.check_triple(board):
            return False
        return True

        