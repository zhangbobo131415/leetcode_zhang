#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#
# https://leetcode-cn.com/problems/search-a-2d-matrix-ii/description/
#
# algorithms
# Medium (37.08%)
# Total Accepted:    9.1K
# Total Submissions: 24.6K
# Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n5'
#
# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
# 
# 
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
# 
# 
# 示例:
# 
# 现有矩阵 matrix 如下：
# 
# [
# ⁠ [1,   4,  7, 11, 15],
# ⁠ [2,   5,  8, 12, 19],
# ⁠ [3,   6,  9, 16, 22],
# ⁠ [10, 13, 14, 17, 24],
# ⁠ [18, 21, 23, 26, 30]
# ]
# 
# 
# 给定 target = 5，返回 true。
# 
# 给定 target = 20，返回 false。
# 
#
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i = matrix.__len__() - 1
        if i < 0:
            return False
        maxrow = len(matrix[0])
        j = 0  #从矩阵的左下角开始
        while i >= 0 and j < maxrow:
            if matrix[i][j] == target:
                return True
            else:
                if matrix[i][j] < target:
                    j += 1    #这一列元素均小于target，j自增1即删除第j列
                else:
                    i -= 1    #这一行元素均大于target，i自增1即删除第i行

        return False
        

