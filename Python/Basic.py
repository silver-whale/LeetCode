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

    def q6(n):
        answer = 0

        while n>0:
            answer += n%10
            n //= 10
        return answer

    def q7(n):
        if math.sqrt(n) == int(math.sqrt(n)) : return ((math.sqrt(n)+1)**2)
        else: return -1

    def q8(n):
        answer = []
        
        while n>0:
            answer.append(n%10)
            n//=10
            
        return answer
    
    def q9(s):
        answer = True
            
        P = s.count('p') + s.count('P')
        Y = s.count('y') + s.count('Y')
        
        if P==0 and Y==0: return True
        elif P==Y: return True
        else: return False

    def q10(x):
        hashad = 0
        temp = x
        while temp>0:
            hashad += temp%10
            temp //= 10
        if x%hashad == 0:
            return True
        else: return False

    def q11(n):
        answer = []
        
        while n>0:
            answer.append(str(n%10))
            n //= 10
        
        result = ''.join(sorted(answer, reverse=True))
        
        return int(result)

    def q12(x, n):
        answer = []
        count = x
        
        for i in range(n):
            answer.append(count)
            count += x
            
        return answer

    def q13(n):
        for i in range(2, n):
            if n%i==1:
                return i
        
    def q14(num):
        count = 0
        
        while(num!=1):
            if num%2==0: num/=2
            elif num%2==1:
                num *= 3
                num += 1
            count += 1
            if(count == 500): return -1
        return count

    def q15(a, b):
        if a==b: return a
        
        answer = 0
        for i in range(min(a,b), max(a,b)+1):
            answer += i
        
        return answer

    def q16(phone_number):
        for i in range(0, len(phone_number)-4):
            phone_number = phone_number[:i] + '*' + phone_number[i+1:]
        return phone_number

    def q17(arr, divisor):
        answer = []
        
        for a in arr:
            if a%divisor == 0:
                answer.append(a)
        if answer:
            return sorted(answer)
        else: return [-1]

    def q18(arr):
        arr.remove(min(arr))
        if not arr: return [-1]
        else: return arr

    def q19(absolutes, signs):
        answer = 0
        for i in range(len(signs)):
            if signs[i]:
                answer += absolutes[i]
            else:
                answer -= absolutes[i]
                
        return answer

    def q20(numbers):
        answer = 0
        for i in range(10):
            if i not in numbers:
                answer += i
        return answer

    def q21(n):
        if n%2 == 0:
            return "수박"*(n//2)
        else:
            return "수박"*(n//2) + "수"

    def q22(s):
        length = len(s)
        
        if length%2==0:
            return s[length//2-1] + s[(length//2)]
        else:
            return s[length//2]

    def q23(a, b):
        answer = 0
        for i in range(len(a)):
            answer += a[i] * b[i]
        return answer

    def q24(s):
        return ''.join(sorted(s,reverse=True))

    def q25(s):
        nums = [int(i) for i in s.split(' ')]
        return str(min(nums))  + " " + str(max(nums))

    def q26(s):
        if len(s) != 4 and len(s) !=6: return False
        for c in s:
            if c.isalpha(): return False
        return True

    def q27(left, right):
        answer = 0
        for num in range(left, right+1):
            count = 0
            sqNum = int(math.sqrt(num))
            for i in range(1, sqNum+1):
                if num%i == 0:
                    if i != num//i: count += 2
                    else: count += 1
            if count%2 == 0:
                answer += num
            else:
                answer -= num
            
        return answer