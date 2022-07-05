class Leetcode542:
    def updateMatrix(self, mat):
        q, m, n = [], len(mat), len(mat[0])

        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0: 
                    mat[i][j] = -1
                else:
                    q.append((i,j))

        for i, j in q:
            for r, c in ((i+1, j), (i, j+1), (i-1, j), (i, j-1)):
                # 0에서 시작하여 주변의 칸들의 거리를 1씩 증가시킴
                count = mat[i][j] + 1
                if 0<=r<m and 0<=c<n and mat[r][c]==-1:
                    mat[r][c] = count
                    q.append((r,c))
        
        return mat
