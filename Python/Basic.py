import math

class solution:
    def q1(sides):
        Ssides = sorted(sides)
        print(Ssides)
        if Ssides[0]+Ssides[1] > Ssides[2]: return 1
        else: return 2

    def q2(my_string, n):
        answer = ''
        for s in my_string:
            answer += s*n
        return answer

    def q3(n):
        sn = int(n**(1/2))
        answer = []
        for i in range(1, sn+1):
            if n%i == 0:
                answer.append(i)
                answer.append(n/i)
        return sorted(answer)

    def q4(n):
        if math.sqrt(n) == int(math.sqrt(n)): return 1
        else: return 2

    def q5(n):
        if n==0: return 0
        answer = 0
        sqN = int(math.sqrt(n))
        for i in range(1, sqN+1):
            if n%i == 0:
                answer += i
                if i != n//i:   
                    answer += n//i
        return answer
