class Leetcode130:
    def solve(self, board: List[List[str]]) -> None:
        queue = []

        for r in range(len(board)):
            for c in range(len(board[0])):
                # 가에 있는 'O'들을 찾기 위함
                if (r in [0, len(board)-1] or c in [0, len(board[0])-1]) and board[r][c] == 'O':
                    queue.append((r, c))
        
        # 가에 있었던 O와 붙어있었던 것들은 V로 바뀜
        while queue:
            r, c = queue.pop(0)
            if 0<=r<len(board) and 0<=c<len(board[0]) and board[r][c] == 'O':
                board[r][c] = 'V'
                queue.append((r-1, c))  
                queue.append((r+1, c))
                queue.append((r, c-1))  
                queue.append((r, c+1))
            
        # 중앙에 동떨어진 것들은 X로 바뀜
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'V':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'