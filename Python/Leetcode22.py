class Leetcode22:
    def generateParenthesis(self, n: int) -> List[str]:

        def dfs(par, open, close):
            if len(par) == 2*n: result.append(par)
            if open<close: return


            # 함수 부를 때마다 가지치기 -> elif 아니고 if문
            if open<n:
                dfs(par + "(", open + 1, close)

            if open > close:
                dfs(par + ")", open, close + 1)


        result = []
        dfs("", 0, 0)

        return result