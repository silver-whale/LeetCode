class Leetcode413:
    def numberOfArithmeticSlices(self, nums):
        N = len(nums)

        if N<3: return 0

        dp = [0] * (N+1)

        for i in range(2, N):
            if nums[i] - nums[i-1] == nums[i-1]-nums[i-2]:
                opt[i] = opt[i-1] + 1


    def slidingwindow(self, nums):
        N = len(nums)
        if N<=2: return 0

        result = 0

        diff = nums[1]-nums[0]

        # elemNum = (number of elements - 2)
        elemNum = 0

        for i in range(1, N-1):
            if nums[i+1] - nums[i] == diff:
                elemNum += 1
            else:
                # 원소 n까지의 길이 3 이상의 부분합의 개수는 1~n-2까지의 합과 같음
                # 그런데 이미 elemNum이 n-2이기 때문에 1~elemNum까지의 합이 결과가 됨
                result += elemNum * (elemNum+1) // 2
                elemNum = 0
                diff = nums[i+1]-nums[i]
        
        if elemNum:
            result += elemNum * (elemNum+1) // 2

        return result




