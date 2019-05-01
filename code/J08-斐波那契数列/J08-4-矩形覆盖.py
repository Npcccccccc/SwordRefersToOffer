# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0 or not number:
            return 0
        
        if number == 1:
            return 1
        elif number == 2:
            return 2

        n1 = 2
        n2 = 1
        ans = 0
        for i in range(3, number + 1):
            ans = n1 + n2
            n1, n2 = ans, n1
        
        return ans