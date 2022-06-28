class Leetcode557:
    def reverseWords(self, s: str) -> str:
        words = []
        for w in s.split():
            words.append(w)

        answer = ''

        for w in range(len(words)):
            answer += words[w][::-1]
            if (w<len(words)-1):
                answer += ' '

        return answer