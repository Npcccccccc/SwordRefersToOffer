# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2:
            return False
        return self.DoesTree1HaveTree2(pRoot1, pRoot2) or self.DoesTree1HaveTree2(pRoot1.left, pRoot2) or self.DoesTree1HaveTree2(pRoot1.right, pRoot2)
        

    def DoesTree1HaveTree2(self, pRoot1, pRoot2):
        if not pRoot2:
            return True
        if not pRoot1 or pRoot1.val != pRoot2.val:
            return False
        return self.DoesTree1HaveTree2(pRoot1.left, pRoot2.left) and self.DoesTree1HaveTree2(pRoot1.right, pRoot2.right)