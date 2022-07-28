from unittest.main import main


class Leetcode120:
    def minimumTotal(self, triangle):
        # dp -> 맨 아랫줄부터 한 칸씩 올라가며 그 줄까지의 최소합을 저장함
        # 맨 아랫줄 밑에 모두 0인 한 줄이 더 있다고 가정 -> len(triangle)+1
        dp = [0] * (len(triangle)+1)
        # dp = [0 for i in range(len(triangle)+1)]

        for row in triangle[::-1]:
            for i, n in enumerate(row):
                dp[i] = n + min(dp[i], dp[i+1])
        
        return dp[0]

# def main():
#     test = Leetcode120()
#     test.minimumTotal([0])

# if __name__=="__main__":
#     main()