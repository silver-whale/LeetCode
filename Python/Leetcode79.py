class Leetcode79:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return False

        m, n = len(board), len(board[0])

        def dfs(index, i, j) -> bool:
            # 도착한 칸의 알파벳 != 문자의 해당 인덱스의 알파벳
            # 해당 솔루션에서는 '#'로 값을 변경했기 때문에 방문한 칸은 무조건 word[index]와 값이 다를 수밖에 없음
            if i<0 or i>=m or j<0 or j>=n or word[index] != board[i][j]:
                return False

            if index == len(word)-1:
                return True

            # 현재 값 백업
            curr = board[i][j]

            # Same as visited[i][j] = True
            board[i][j] = '#'

            found = dfs(index+1, i+1, j) or dfs(index+1, i-1, j) or dfs(index+1, i, j+1) or dfs(index+1, i, j-1)

            # 순회가 끝난 뒤에 복구
            board[i][j] = curr

            return found

        # any(): 하나라도 True가 있으면 True => or
        # all(): 모두 True여야 True => and
        return any(dfs(0, i, j) for i in range(m) for j in range(n))


    # Visited 배열 사용 시
    def exist2(self, board, word):
        if not board:
            return False
        r, c = len(board), len(board[0])
        visited = [[False for i in range(c)] for j in range(r)]
        for i in range(r):
            for j in range(c):
                if self.dfs2(board, word, visited, i, j):
                    return True
        return False

    def dfs2(self, board, word, visited, i, j):
        if not word:
            return True
        if i < 0 or i == len(board) or j < 0 or j == len(board[0]) \
        or visited[i][j] or word[0] != board[i][j]:
            return False
        visited[i][j] = True
        res = self.dfs2(board, word[1:], visited, i+1, j) or \
              self.dfs2(board, word[1:], visited, i-1, j) or \
              self.dfs2(board, word[1:], visited, i, j-1) or \
              self.dfs2(board, word[1:], visited, i, j+1)
        visited[i][j] = False
        return res