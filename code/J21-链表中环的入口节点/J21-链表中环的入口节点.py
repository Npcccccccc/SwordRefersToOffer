# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def meetingNode(self, head):
        # 判断特殊输入
        if not head:
            return None

        p_slow = head.next
        if not p_slow:
            return None
        p_fast = p_slow.next

        while p_fast != None and p_slow != None:
            if p_fast == p_slow:
                return p_slow
            
            p_slow = p_slow.next
            #分两步走，确保p_fast不会因为第一步走到了None域，而导致走第二步时报错
            p_fast = p_fast.next
            if p_fast != None:
                p_fast = p_fast.next
        
        return None

    def entryNodeOfLoop(self, head):
        # 如果存在环，找到快慢指针相遇节点; 若环不存在，返回None
        p_meet = self.meetingNode(head)
        if not p_meet:
            return p_meet
        
        # 计算环中节点的个数,从相遇节点开始计数，所以loop从1开始
        loop = 1
        p_temp = p_meet
        while p_temp != p_meet:
            p_temp = p_temp.next
            loop += 1
        
        p_first = head
        p_second = head
        for i in range(loop):
            p_first = p_first.next
        while p_first != p_second:
            p_first = p_first.next
            p_second = p_second.next
        
        return p_second