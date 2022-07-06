class Leetcode77:
    def combine(self, n, k):
        result = []

        def backtracking(start, combi):
            if len(combi) == k:
                result.append(combi.copy())
                return

            # n should be included
            for i in range(start, n+1):
                combi.append(i)
                backtracking(i+1, combi)
                combi.pop()
        
        backtracking(1, [])

        return result