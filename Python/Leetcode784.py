class Leetcode784:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = ['']

        for c in s:
            if c.isalpha():
                result = [prev + j 
                        for prev in result
                        for j in [c.upper(), c.lower()]]
            else:
                result = [prev + c for prev in result]
        return result