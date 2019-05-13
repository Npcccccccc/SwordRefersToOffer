# -*- coding:utf-8 -*-
class Solution:
    print_number = []
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        if matrix == None or cols <= 0 or rows <= 0:
            return
        
        start = 0

        while cols > start * 2 and rows > start * 2:
            self.printMatrixInCircle(matrix, cols, rows, start)
            start += 1
        
        return self.print_number
        
    def printMatrixInCircle(self, matrix, cols, rows, start):
        endX = cols - 1 - start
        endY = rows - 1 - start

        for i in range(start, endX+1):
            number = matrix[start][i]
            self.print_number.append(number)
        
        if start < endY:
            for i in range(start+1, endY+1):
                number = matrix[i][endX]
                self.print_number.append(number)
            
        if start < endX and start < endY:
            for i in range(endX-1, start-1, -1):
                number = matrix[endY][i]
                self.print_number.append(number)

        if start < endX and start < endY-1:
            for i in range(endY-1, start, -1):
                number = matrix[i][start]
                self.print_number.append(number)