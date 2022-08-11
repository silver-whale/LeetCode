from collections import deque
class Leetcode1091:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1

        N = len(grid)

        # List는 O(n), Set는 O(1)이라서 set를 사용
        visited = set()
        queue = deque()

        # [x, y, depth]
        queue.append([0, 0, 1])

        while queue:
            [r, c, depth] = queue.popleft()
            # Finished
            if r==N-1 and c==N-1:
                return depth

            for [nr, nc] in [[r-1, c-1],[r-1, c],[r-1, c+1],[r, c-1],[r, c+1],[r+1, c-1],[r+1, c],[r+1, c+1]]:
                if ((nr, nc) not in visited and 0<=nr<N and 0<=nc<N and grid[nc][nr]==0):
                    visited.add((nr, nc))
                    queue.append([nr, nc, depth+1])
        
        return -1










