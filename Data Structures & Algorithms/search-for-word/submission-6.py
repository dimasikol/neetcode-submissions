class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        row = len(board)
        column = len(board[0])
        starts = [(i, j) for i in range(row) for j in range(column) if board[i][j] == word[0]]
        visited = set()

        def check(row,col,i,j):
            if  0 <= i <row and 0 <= j and j < col:
                return True
            return False

        if not starts:
            return False

        if len(word)==1:
            return True

        def backtrack(i, j, index):
            if index == len(word) :
                return True
            if check(row,column, i,j) == False or word[index] != board[i][j] or (i,j) in visited:
                return False

            visited.add((i,j))

            for ii, jj in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                if backtrack(ii,jj, index+1):
                    print(visited)
                    return True

            visited.remove((i,j))

            return False

        for i,j in starts:
            if backtrack(i,j, 0):
                return True
        return False
