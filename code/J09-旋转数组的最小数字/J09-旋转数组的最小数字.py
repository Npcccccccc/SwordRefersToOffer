# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return 0
        
        # 如果第一个元素小于末尾的元素，意味着数组可能旋转了0个元素(原序)
        index_start = index_middle = 0
        index_end = len(rotateArray)-1
        while rotateArray[index_start] >= rotateArray[index_end]:
            # 如果两者距离相差1，则指针2指向最小数字
            if index_end - index_start == 1:
                index_middle = index_end
                break
            
            index_middle = (index_start + index_end) / 2
            
            if rotateArray[index_start] == rotateArray[index_end] and rotateArray[index_start] == rotateArray[index_middle]:
                ans = rotateArray[index_start]
                for i in range(index_start+1, index_end+1):
                    if ans > rotateArray[i]:
                        ans = rotateArray[i]
                return ans

            if rotateArray[index_middle] >= rotateArray[index_start]:
                index_start = index_middle
            elif rotateArray[index_middle] <= rotateArray[index_end]:
                index_end = index_middle
        return rotateArray[index_middle]

