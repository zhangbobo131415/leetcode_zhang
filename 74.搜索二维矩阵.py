#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#
# https://leetcode-cn.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (33.46%)
# Total Accepted:    6.8K
# Total Submissions: 20.3K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,50]]\n3'
#
# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
#
#
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
#
#
# 示例 1:
#
# 输入:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 3
# 输出: true
#
#
# 示例 2:
#
# 输入:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 13
# 输出: false
#
#
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col=len(matrix)
        if col==0:
            return False
        row=len(matrix[0])
        if row==0:
            return False
        for i in range(col):
            if target<=matrix[i][row-1]:
                break
        for j in range(row):
            if matrix[i][j]==target:
                return True
        return False



        