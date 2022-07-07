class Leetcode70:
    def climbStairs(self, n):
        if n<=0: return 0
        if n==1: return 1
        if n==2: return 2

        one_step_before, two_steps_before, answer = 2, 1, 0

        for i in range(2, n):
            # 특정 수 x까지 가는 방법의 수는 
            # (x-1)까지 가는 방법의 수 + (x-2)까지 가는 방법의 수
            answer = one_step_before + two_steps_before
            # (x-1)의 경우의 수는 (x-2)에서 한 칸 올라오는 것밖에
            two_steps_before = one_step_before
            one_step_before = answer

        return answer