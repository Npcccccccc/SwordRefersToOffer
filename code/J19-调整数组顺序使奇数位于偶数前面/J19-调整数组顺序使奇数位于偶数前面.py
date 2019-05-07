# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        if not array:
            return array
        new_list = list()
        odd_index = 0
        for number in array:
            if self.judgeOdd(number):
                new_list.insert(odd_index, number)
                odd_index += 1
            else:
                new_list.append(number)
        return new_list

    # 判断一个数是否使奇数，是的话返回true，否的是返回fault
    def judgeOdd(self, number):
        # 使用&运算来快速判断奇偶
        if number & 1 != 0:
            return True
        else:
            return False