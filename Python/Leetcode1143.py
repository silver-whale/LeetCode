class Leetcode1143:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N, M = len(text1), len(text2)

        # dp(i,j) -> text1[:i]와 text2[:j]의 
        dp = [[0 for i in range(M+1)] for i in range(N+1)]


        # dp[i+1][j+1] -> text[i] is text[:i+1]'s last word
        for i in range(N):
            for j in range(M):
                # 만약 맨 끝이 같으면 이전 거 + 한 글자
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j]+1
                else:
                    # 일치하는 게 없으면 기존 값 중 가장 큰 거 유지
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

        # text1[:N], text2[:M]
        return dp[-1][-1]