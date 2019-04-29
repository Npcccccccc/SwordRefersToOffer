# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target:int, array)->bool:
        row = 0
        col = len(array[0])-1
        while row < len(array) and col >= 0:
            if target > array[row][col]:
                row += 1
            elif target < array[row][col]:
                col -= 1
            else:
                return True
        return False