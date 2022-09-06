class Leetcode62:
    def uniquePaths(self, m: int, n: int) -> int:
        # 맨 첫 칸이 1이라서 1로 설정, 나머지는 어차피 밑의 이중 for문에서 값 변경됨
        dp = [ [1 for i in range(n)] for i in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]