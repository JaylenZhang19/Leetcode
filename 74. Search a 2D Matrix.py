class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        if not row:
            return False
        column = len(matrix[0])
        if not column:
            return False
        if target < matrix[0][0] or target > matrix[row-1][column-1]:
            return False
        top, down = 0, row - 1
        while top < down:
            if target < matrix[top][0]:
                return False
            if target > matrix[down][0]:
                top = down
                break
            mid = top + (down - top) // 2
            if matrix[mid][0] <= target < matrix[mid+1][0]:
                top = down = mid
            elif matrix[mid][0] > target:
                down = mid - 1
            else:
                top = mid + 1
        left, right = 0, column - 1
        while left < right:
            mid = left + (right - left) // 2
            if matrix[top][mid] == target:
                return True
            if matrix[top][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if matrix[top][left] == target:
            return True
        else:
            return False