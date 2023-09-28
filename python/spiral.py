class Solution:
    result = []
    def helper(self, x, y, matrix):
        x_max = len(matrix[0])
        y_max = len(matrix)
        self.result.append(matrix[y][x])

        matrix[y][x] = ""
        if x + 1 in range(0, x_max) and matrix[y][x+1]:
            self.helper(x+1, y, matrix)
        elif y + 1 in range(0, y_max) and matrix[y+1][x]:
            self.helper(x, y+1, matrix)
        elif x - 1 in range(0, x_max) and matrix[y][x-1]:
            self.helper(x-1, y, matrix)
        elif y - 1 in range(0, y_max) and matrix[y-1][x]:
            self.helper(x, y-1, matrix)

    def spiralOrder(self, matrix):
        if not matrix[0][0]:
            return []

        self.helper(0, 0, matrix)
        return self.result


test = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
# 1  2  3  4
# 5  6  7  8
# 9 10 11 12
# [1, 2, 3, 6, 9, '', '', '', 5]
res = test.spiralOrder(matrix)
print(res)
