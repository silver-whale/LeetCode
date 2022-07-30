class Leetcode844:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def strip_str(S : str) -> str:
            result = []
            for c in S:
                if c=='#':
                    if len(result)>=1:
                        result.pop()
                else:
                    result.append(c)
            return result

        return strip_str(s) == strip_str(t)