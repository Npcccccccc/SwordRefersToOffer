# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack_one = list()
        self.stack_two = list()
    def push(self, node):
        self.stack_one.append(node)
    def pop(self):
        if not self.stack_two:
            while self.stack_one:
                self.stack_two.append(self.stack_one.pop())
        return self.stack_two.pop()