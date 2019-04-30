# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        ans = [0, 1]
        if n < 2:
            return ans[n]
        num1 = 1
        num2 = 0
        FibN = 0
        i = 2
        while i <= n:
            FibN = num1 + num2
            num1, num2 = FibN, num1
            i += 1
        return FibN