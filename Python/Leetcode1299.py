class Java.Solution:
    def replaceElements(self, arr:List[int]) -> List[int]:
        # initial max = -1
        # reverse iteration
        # arr[i] = max(arr[i], arr[i+1])을 역순으로 오면 오른쪽 값은 무조건 최댓값
        # new max = max(oldmax, arr[i])

        rightMax = -1

        for i in range(len(arr)-1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr