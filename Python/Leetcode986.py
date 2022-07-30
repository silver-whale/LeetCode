# 공통 시작점: 두 시작점 중 최대값
# 공통 끝점: 두 끝점 중 최소값

class Leetcode986:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        idxA, idxB = 0, 0
        sizeA, sizeB = len(A), len(B)

        answer = []

        while idxA<sizeA and idxB<sizeB:
            startA, endA = A[idxA]
            startB, endB = B[idxB]

            commonStart = max(startA, startB)
            commonEnd = min(endA, endB)

            if commonStart <= commonEnd:
                answer.append([commonStart, commonEnd])
            
            if endA<=endB:
                idxA += 1
            else:
                idxB += 1
            
        return answer

