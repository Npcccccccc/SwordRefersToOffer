# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # 先构造根节点
        roofNode = TreeNode(pre[0])
        roofNode.left = roofNode.right = None
        # 判读错误条件
        if len(pre) == 1:
            if len(tin) == 1:
                if pre != tin:
                    return None
                else:
                    return roofNode
        # 在中序遍历中找到根节点
        roofLocation = 0
        while roofLocation < len(tin) and tin[roofLocation] != roofNode.val:
            roofLocation += 1
        # 如果未找到，则抛出错误
        if roofLocation == len(tin)-1 and tin[roofLocation] != roofNode.val:
            return None
        # 使用递归构造左右子树; 注意传入的参数取值，不能传入空数组
        if pre[1:roofLocation+1] and tin[:roofLocation]:
            roofNode.left = self.reConstructBinaryTree(pre[1:roofLocation+1], tin[:roofLocation])
        if pre[roofLocation+1:] and tin[roofLocation+1:]:
            roofNode.right = self.reConstructBinaryTree(pre[roofLocation+1:], tin[roofLocation+1:])
        return roofNode