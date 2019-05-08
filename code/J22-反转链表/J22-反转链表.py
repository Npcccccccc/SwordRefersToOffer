# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        p_reverse_head = None
        p_node = pHead
        p_pre = None
        while p_node != None:
            p_next = p_node.next
            if p_next == None:
                p_reverse_head = p_node
            p_node.next = p_pre
            p_pre = p_node
            p_node = p_next
        return p_reverse_head