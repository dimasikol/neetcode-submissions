class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        # Собираем все стартовые позиции
        starts = [(i, j) for i in range(rows) for j in range(cols) if board[i][j] == word[0]]
        if not starts:
            return False
        if len(word) == 1:
            return True

        visited = set()

        def backtrack(i: int, j: int, index: int) -> bool:
            # Если дошли до конца слова — успех
            if index == len(word):
                return True
            # Проверка границ, совпадения буквы и того, что клетка не посещена
            if not (0 <= i < rows and 0 <= j < cols) \
               or board[i][j] != word[index] \
               or (i, j) in visited:
                return False

            visited.add((i, j))
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if backtrack(i + di, j + dj, index + 1):
                    return True
            visited.remove((i, j))
            return False

        for i, j in starts:
            if backtrack(i, j, 0):
                return True
        return False