class Solution:
    def helpify2(self,board):
        duble = set()
        for i in range(len(board)):
            if board[i].isdigit() and board[i] in duble:
                return False
            else:
                duble.add(board[i])
        return True
    def helpify(self,board):
        for i in range(len(board)):
            duble = set()
            for k in range(len(board[i])):
                if board[i][k].isdigit() and board[i][k] in duble:
                    return False
                else:
                    duble.add(board[i][k])
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if self.helpify(board) and self.helpify([i for i in zip(*board)]):
            for i in range(3):
                q = board[i*3:(i+1)*3]
                for j in range(3):
                    r = []
                    for s in q:
                        r+= s[j*3:(j+1)*3]
                    if False==self.helpify2(r):
                        return False 
            return True
        else:
            return False