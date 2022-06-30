class Leetcode733:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(i, j):
            image[i][j] = color

            # dx = [-1, 0, 1, 0]
            # dy = [0, -1, 0, 1]

            # for d in range(4):
            #     if 0<=i+dx[d]<m and 0<=j+dy[d]<n and image[i+dx[d]][j+dy[d]] == cur:
            #         dfs(i+dx[d], j+dy[d])

            for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0<=x<m and 0<=y<n and image[x][y] == cur:
                    dfs(x, y)

        cur, m, n = image[sr][sc], len(image), len(image[0])

        if cur != color: dfs(sr, sc)

        return image

