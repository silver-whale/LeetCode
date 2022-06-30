class Leetcode695:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        def dfs(r, c):
            # 1이 아니면 return 0
            if r<0 or r==m or c<0 or c==n or grid[r][c]==0:
                return 0
            # dfs[r][c]가 1이면 우선 answer 1로 설정 후 해당 영역 0으로 바꿈
            answer = 1
            grid[r][c] = 0
            # 재귀적으로 주변 땅 탐색, 주변 땅에 1이 있으면 기존 answer에 더해지고
            # 만약 맨 위의 if문에 걸리면 0이 되어서 더해지지 않음
            for i in range(4):
                answer += dfs(r+dx[i], c+dy[i])
            return answer

        answer = 0
        for r in range(m):
            for c in range(n):
                answer = max(answer, dfs(r,c))
        return answer

        def bfs(r, c):
            # queue에 삽입 후 0으로 바꿈
            q = deque([(r,c)])
            grid[r][c] = 0

            answer = 0
            while q:
                r, c = q.popleft()
                answer += 1
                for i in range(4):
                    nr, nc = r+dx[i], c+dy[i]
                    if nr<0 or nr==m or nc<0 or nc==n or grid[nr][nc]==0: continue
                    grid[nr][nc] = 0
                    q.append(nr, nc)
            return answer

        answer = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    answer = max(answer, bfs(r, c))
        
        return answer