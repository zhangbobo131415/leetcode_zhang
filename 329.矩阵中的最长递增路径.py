#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] 矩阵中的最长递增路径
#
# https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (36.66%)
# Total Accepted:    1.4K
# Total Submissions: 4K
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# 给定一个整数矩阵，找出最长递增路径的长度。
#
# 对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。
#
# 示例 1:
#
# 输入: nums =
# [
# ⁠ [9,9,4],
# ⁠ [6,6,8],
# ⁠ [2,1,1]
# ]
# 输出: 4
# 解释: 最长递增路径为 [1, 2, 6, 9]。
#
# 示例 2:
#
# 输入: nums =
# [
# ⁠ [3,4,5],
# ⁠ [3,2,6],
# ⁠ [2,2,1]
# ]
# 输出: 4
# 解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
#
#
#


#将原问题分解为从上到下从左到右寻找递增或递减最长序列问题即可
#注意使用动态规划
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        col_matrix = len(matrix)
        if col_matrix == 0:
            return 0

        row_matrix = len(matrix[0])
        if row_matrix == 0:
            return 0
        res_matrix = [[0 for i in range(row_matrix)]
                      for j in range(col_matrix)]
        res_matrix[0][0] = 1
        result = 1
        #先获得递减子序列
        for i in range(1, col_matrix):
            if matrix[i][0] < matrix[i - 1][0]:
                res_matrix[i][0] = res_matrix[i - 1][0] + 1
                result = max(result, res_matrix[i][0])
            else:
                res_matrix[i][0] = 1
        for i in range(1, row_matrix):
            if matrix[0][i] < matrix[0][i - 1]:
                res_matrix[0][i] = res_matrix[0][i - 1] + 1
                result = max(result, res_matrix[0][i])
            else:
                res_matrix[0][i] = 1


        tem1 = tem2 = 0
        for i in range(1, col_matrix):
            for j in range(1, row_matrix):
                if matrix[i][j] < matrix[i - 1][j]:
                    tem1 = res_matrix[i - 1][j] + 1
                if matrix[i][j] < matrix[i][j - 1]:
                    tem2 = res_matrix[i][j - 1] + 1
                res_matrix[i][j] = max(tem1, tem2, 1)
                result = max(result, res_matrix[i][j])
                tem1 = tem2 = 0




        for i in range(1, col_matrix):
            if matrix[i][0] > matrix[i - 1][0]:
                res_matrix[i][0] = res_matrix[i - 1][0] + 1
                result = max(result, res_matrix[i][0])
            else:
                res_matrix[i][0] = 1
        for i in range(1, row_matrix):
            if matrix[0][i] > matrix[0][i - 1]:
                res_matrix[0][i] = res_matrix[0][i - 1] + 1
                result = max(result, res_matrix[0][i])
            else:
                res_matrix[0][i] = 1
        tem1 = tem2 = 0
        for i in range(1, col_matrix):
            for j in range(1, row_matrix):
                if matrix[i][j] > matrix[i - 1][j]:
                    tem1 = res_matrix[i - 1][j] + 1
                if matrix[i][j] > matrix[i][j - 1]:
                    tem2 = res_matrix[i][j - 1] + 1
                res_matrix[i][j] = max(tem1, tem2, 1)
                tem1 = tem2 = 0
                result = max(result, res_matrix[i][j])

        return result
