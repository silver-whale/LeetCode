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

    def q28(s):
        answer = list(s)
        
        if answer[0].isalpha():
            answer[0] = answer[0].upper()
            
        for i in range(1, len(answer)):
            if answer[i-1] == " " and answer[i].isalpha():
                answer[i] = answer[i].upper()
            elif answer[i].isalpha():
                answer[i] = answer[i].lower()
        
        return "".join(answer)

    def q29(arr1, arr2):
        m, n = len(arr1), len(arr1[0])
        answer = [[0 for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                answer[i][j] = arr1[i][j] + arr2[i][j]
            
        return answer

    def q30(price, money, count):
        total = count*((2*price)+(count-1)*price)//2
        
        if money>=total: return 0
        else: return total-money

    def q31(n, m):
        def gcd(a, b):
            while (b>0):
                a, b = b, a%b
            return a

        gc = gcd(max(n, m), min(n, m))
        
        # x*y를 최대공약수로 나눈 것이 최소공배수가 됨
        lm = n*m // gc
        
        return [gc, lm]

    def q32(A,B):
        sA = sorted(A)
        sB = sorted(B, reverse=True)
        
        answer = 0
        
        for i in range(len(sA)):
            answer += sA[i]*sB[i]
        
        return answer

    def q33(x):
        count = 0
        zeros = 0
        
        while True:
            if x == "1": break
            
            zeros += x.count("0")
            x = x.replace("0", "")
            
            # 앞에 0b가 붙어서 떼줘야 함
            x = bin(len(x))[2:]
            
            count += 1
        
        return [count, zeros]

    def q34(s):
        open = 0
        
        if s[0] == ')': return False

        for c in s:
            if open < 0: return False
        
            if c=='(':
                open += 1
            else:
                open -= 1
        
        if open != 0: return False
        else: return True

    def q35(arr):
        last = -1
        answer = []
        for a in arr:
            if last != a:
                answer.append(a)
                last = a

        return answer

    def q36(n):
        # 연속된 자연수라 FOR문
        answer = 1
        for i in range(1, n//2+1):
            num = 0
            # 차례로 올려가며 더함
            for j in range(i, n+1):
                num += j
                if num == n:
                    answer += 1
                    break
                if num>n:
                    break
        return answer

    def q37(s):
        answer = []
        words =  s.split(" ")
        
        for word in words:
            temp = ""
            for w in range(len(word)):
                if w%2 == 0:
                    temp += word[w].upper()
                else:
                    temp += word[w].lower()
            answer.append(temp)
        
        return " ".join(answer)


    def q38(n):
        answer = 0
        
        # 3진법 변환
        tri = ""
        while n>0:
            n, m = divmod(n, 3)
            tri += str(m)
        # 원래는 [::-1] 해줘야 하지만 앞뒤로 뒤집는 과정 때문에 삭제
        
        for i in range(len(tri)):
            answer += int(tri[i]) * (3**(len(tri)-i-1))
        
        return answer

    def q39(n):
        # fib[0] = 0, fib[1] = 1
        fib = [i for i in range(n+1)]
        
        for i in range(2, n+1):
            fib[i] = fib[i-1] + fib[i-2]

        return fib[n]%1234567
        
    def q40(d, budget):
        d = sorted(d)
        while budget<sum(d):
            d.pop()
        return len(d)

    def q41(n):
        ones = bin(n).count('1')
        while True:
            n += 1
            if bin(n).count('1') == ones: return n

    def q42(s, n):
        answer = ""
        for c in s:
            if c == " ":
                answer += " "
            else:
                res = ord(c) + n
                if ord(c) <= 90:
                    print("C is upper")
                    if res > ord('Z'):
                        answer += chr(ord('A') + res - ord('Z') - 1)
                    else:
                        answer += chr(res)
                else:
                    print("C is lower")
                    if res > ord('z'):
                        answer += chr(ord('a') + res - ord('z') - 1)
                    else:
                        answer += chr(res)    
        return answer

    def q43(n, arr1, arr2):
        answer = []
        for i in range(len(arr1)):
            a, b = bin(arr1[i])[2:].zfill(n), bin(arr2[i])[2:].zfill(n)
            line = ""
            for j in range(n):
                if a[j] == '1' or b[j] == '1':
                    line += '#'
                else:
                    line += ' '
            answer.append(line)
        return answer


    def q44(brown, yellow):
        nAddm = (brown+4)//2
        
        for n in range(nAddm//2+1):
            m = nAddm - n
            if n*m - brown == yellow:
                return [m, n]

    def q45(sizes):
        rows, cols = [], []
        for s in sizes:
            rows.append(max(s))
            cols.append(min(s))
        return max(rows)*max(cols)

    def q46(n, words):
        count = [0 for i in range(n)]
        
        last = ' '
        
        for w in range(len(words)):
            count[w%n] += 1

            if len(words[w]) == 1: return [w%n+1, count[w%n]]
            
            if w != 0:
                if words[w] in words[:w]:
                    return [w%n+1, count[w%n]]
                if words[w][0] != last:
                    return [w%n+1, count[w%n]]
            last = words[w][-1]
            
        return [0, 0]

    def q47(s):
        result = [s[0]]
        
        for i in range(1, len(s)):
            if result and s[i] == result[-1]:
                result.pop()
            else: result.append(s[i])

        if result: return 0
        else: return 1

    def q48(strings, n):
        # N번째 문자열이 같으면 그냥 단어 전체를 비교
        return sorted(strings, key = lambda x: (x[n], x))

    def q49(array, commands):

        answer = []
        for i in range(len(commands)):
            i, j, k = commands[i][0]-1, commands[i][1], commands[i][2]-1
            answer.append(sorted(array[i:j])[k])
        
        return answer

    def q50(s):
        result = s
        numbers = [("0", "zero"), 
                ("1", "one"), 
                ("2", "two"),
                ("3", "three"),
                ("4", "four"),
                ("5", "five"),
                ("6", "six"),
                ("7", "seven"),
                ("8", "eight"),
                ("9", "nine")]
        
        for n in numbers:
            print(n[0], n[1])
            result = result.replace(n[1], n[0])
        
        return int(result)

    def q51(people, limit):
        numPeople = len(people)
        sPeople = sorted(people)
        
        rescued = 0
        boat = 0
        
        firstIndex = 0
        lastIndex = len(sPeople)-1
        
        while rescued < numPeople:

            if firstIndex == lastIndex:
                rescued += 1
                boat += 1
                return boat
            while sPeople[lastIndex] > limit - sPeople[firstIndex]:
                rescued += 1
                boat += 1
                lastIndex -= 1
                if firstIndex >= lastIndex: 
                    return boat + 1
            firstIndex += 1
            lastIndex -= 1
            rescued += 2
            boat += 1
        return boat

    def q52(arr):
        def gcd(a, b):
            a, b = max(a,b), min(a,b)
            while (b>0):    
                a, b = b, a%b
            return a
        
        if len(arr) == 1:
            return arr[0]
        if len(arr) == 2:
            return  arr[0]*arr[1] // gcd(arr[0], arr[1])
        
        first, second = arr[0], arr[1]
        great = 0
        
        i = 1
        
        while i<len(arr)-1:
            great = gcd(first, second)
            first = first*second // great
            i += 1
            second = arr[i]
        
        great = gcd(first, second)
        
        return first*second // great

    def q53(numbers):
        answer = []
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i]+numbers[j] not in answer:
                    answer.append(numbers[i]+numbers[j])
        
        return sorted(answer)

    def q54(number):
        answer = 0
        for i in range(len(number)):
            for j in range(i+1, len(number)):
                if -number[i]-number[j] in number[j+1:]:
                    answer += number[j+1:].count(-number[i]-number[j])
        return answer

    def q55(n,a,b):
        count = 0
        
        while a != b:
            if a % 2 == 1:
                a = a//2 + 1
            else:
                a = a//2
                
            if b % 2 == 1:
                b = b//2 + 1
            else:
                b = b//2
                
            count += 1

    def q56(n):
        if n==1: return 1
        if n==2: return 2

        # DP or Fibo
        dp = [1 for i in range(n+1)]
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        
        return dp[n]%1234567
            
    