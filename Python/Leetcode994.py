class Leetcode994(object):
    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0])
        count = 0
        q = collections.deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # Number of left fresh orange
                    count += 1
                elif grid[i][j] == 2:
                    q.append((i,j,0))
        
        visited = set()

        # (x, y, d): x, y는 좌표, d는 해당 좌표가 썩은 시간
        while q:
            x, y, d = q.popleft()
            for x, y in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0<=x<m and 0<=y<n and (x,y) not in visited and grid[x][y] == 1:
                    visited.add((x, y))
                    count -= 1
                    if count == 0:
                        return d+1
                    q.append((x, y, d+1))
        # if no fresh orange -> return 0, else if fresh orange left -> -1
        return 0 if count == 0 else -1
