class Leetcode139:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = [0]

        for i in range(N):
            for j in dp:
                if s[j:i+1] in wordDict:
                    dp.append(i+1)
                    break
        
        return dp[-1] == N