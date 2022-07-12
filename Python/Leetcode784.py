class Leetcode784:
    def letterCasePermutation(self, s: str):
        answer = ['']

        for c in s:
            if c.isalpha():
                answer = [ans+new for ans in answer for new in [c.upper(), c.lower()]]
            else:
                answer = [ans+c for ans in answer]

        return answer

