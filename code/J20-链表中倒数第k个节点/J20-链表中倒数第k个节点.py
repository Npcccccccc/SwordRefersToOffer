# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # 判断特殊输入;
        # k从1开始计数，输入0无意义
        if not head or k == 0:
            return None
        
        p_first = head
        for i in range(0, k-1):
            if p_first.next != None:
                p_first = p_first.next
            else:
                return None
        
        p_second = head
        # 注意此处第判断条件; 当p_first走到最后一个节点时, p_second正好指向倒数第k个节点;
        # 如果时判断条件为：p_first != None的话，p_first最后指向尾节点的next处，而此时p_second指向倒数第k-1个节点，因为多走了一步
        while p_first.next != None:
            p_first = p_first.next
            p_second = p_second.next
        return p_second