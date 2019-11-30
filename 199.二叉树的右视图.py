#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#
# https://leetcode-cn.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (56.31%)
# Total Accepted:    4.1K
# Total Submissions: 7.3K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
#
# 示例:
#
# 输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:
#
# ⁠  1            <---
# ⁠/   \
# 2     3         <---
# ⁠\     \
# ⁠ 5     4       <---
#
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        tem = []
        res = []
        depth = 1
        if root:
            tem.append((root, depth))
        else:
            return res
        while tem.__len__() >= 1:
            top = tem[0][0]
            depth = tem[0][1]
            if top.right:
                tem.append((top.right, depth + 1))
            if top.left:
                tem.append((top.left, depth + 1))
            if res.__len__() < depth:
                res.append(top.val)
            tem.pop(0)
        return res
