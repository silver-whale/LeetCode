class Leetcode74:
    def searchMatrix(self, matrix : List[List[int]], target : int):
        row, col = 0, len(matrix[0])-1

        while(row<len(matrix) and col >= 0):
            if matrix[row][col] == target:
                return True
            elif target>matrix[row][col]:
                row += 1
            else:
                col -= 1
            
        return False
