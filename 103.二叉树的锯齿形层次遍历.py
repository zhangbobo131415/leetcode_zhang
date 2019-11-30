#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# class Solution:
#     def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
#         tem_queue = []
#         tem_stack = []
#         res = []
#         if root == None:
#             return tem_queue
#         tem_queue.append((root, 1))
#         while len(tem_queue) > 0:
#             tem_node = tem_queue.pop(0)
#             if res.__len__() < tem_node[1]:
#                 res.append([])
#             if tem_node[1] & 1 == 0:
#                 # 偶数层进栈
#                 tem_stack.append(tem_node)
#             else:
#                 #奇数层直接保存在res中
#                 res[tem_node[1]-1].append(tem_node[0].val)
#             if tem_stack.__len__() > 0 and (tem_stack[-1][1] != tem_node[1] or len(tem_queue)==0):
#                 #出栈条件
#                 tem_stack.reverse()
#                 for i in tem_stack:
#                     res[tem_stack[-1][1] - 1].append(i[0].val)
#                 tem_stack.clear()
#             if tem_node[0].left:
#                 tem_queue.append((tem_node[0].left, tem_node[1] + 1))
#             if tem_node[0].right:
#                 tem_queue.append((tem_node[0].right, tem_node[1] + 1))
#         return res

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        tem_queue = []
        res = []
        if root == None:
            return tem_queue
        tem_queue.append((root, 1))
        while tem_queue.__len__() > 0:
            tem_node = tem_queue.pop(0)
            if res.__len__() < tem_node[1]:
                res.append([])
            res[tem_node[1]-1].append(tem_node[0].val)
            if tem_node[0].left:
                tem_queue.append((tem_node[0].left, tem_node[1] + 1))
            if tem_node[0].right:
                tem_queue.append((tem_node[0].right, tem_node[1] + 1))
        for i in range(res.__len__()):
            if i & 1 ==1:
                res[i].reverse()
        return res

