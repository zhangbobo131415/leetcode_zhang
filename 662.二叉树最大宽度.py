#
# @lc app=leetcode.cn id=662 lang=python3
#
# [662] 二叉树最大宽度
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution: 
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        tem_queue = []
        res = []
        if root == None:
            return 0
        level = 1
        level_loc = 0
        width_max = 1
        # level表示层数，level_loc表示其在层内的位置
        tem_queue.append((root, level, level_loc))
        while tem_queue.__len__() > 0:
            cur_node, level, level_loc = tem_queue.pop(0)
            if len(res) < level:
                res.append([])
            # 层次遍历，只保存每层的第一个和最后一个节点的位置信息，
            if len(res[level - 1]) == 2:
                res[level - 1][1] = level_loc
            else:
                res[level-1].append(level_loc)
            if cur_node.left:
                tem_queue.append((cur_node.left, level + 1, level_loc * 2))
                
            if cur_node.right:
                tem_queue.append(
                    (cur_node.right, level + 1, level_loc* 2 + 1))
        for tem in res:
            if len(tem) == 1:
                pass
            else:
                # tem[-1] - tem[0] + 1为该层的宽度
                width_max = max(tem[-1] - tem[0] + 1, width_max)
        return width_max
