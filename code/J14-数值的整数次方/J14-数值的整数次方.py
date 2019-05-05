# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        self.invalidInput = False
        # 判断特殊情况
        if base == 0.0 and exponent < 0:
            return 0.0
    
        absExponent = abs(exponent)
        ans = self.calculatePower(base, absExponent)
        if exponent < 0:
            ans = 1.0 / ans
        return ans
        
    def calculatePower(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        
        ans = self.calculatePower(base, exponent >> 1)
        ans *= ans
        if exponent & 1 == 1:
            ans *= base
        return ans