class Leetcode17:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}

        if len(digits) == 0: return []
        elif len(digits) == 1 : return list(phone[digits])

        # 맨 첫 글자 분리
        head = digits[0]
        body = digits[1:]

        # 분리된 첫 글자의 조합 + 나머지 글자들 재귀
        headComb = phone[head]
        bodyComb = self.letterCombinations(body)

        return [h + b for h in headComb for b in bodyComb]