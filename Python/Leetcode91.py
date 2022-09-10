class Leetcode91:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        N = len(s)

        dp = [0] * (N+1)
        # dp[i+1]이 s[i]까지의 경우의 수
        dp[0] = dp[1] = 1

        for i in range(1, N):
            # 1자릿수는 무조건 범위 안이기 때문에
            # 한 칸 전의 경우의 수 그대로 유지
            if s[i] != '0':
                dp[i+1] += dp[i]
            # 2자릿수의 경우 범위 안이면 두 칸 전의 경우의 수가 유지됨
            if s[i-1]!='0' and 1<=int(s[i-1:i+1])<=26:
                dp[i+1] += dp[i-1]
            
        return dp[N]