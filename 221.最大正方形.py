#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#
# https://leetcode-cn.com/problems/maximal-square/description/
#
# algorithms
# Medium (36.52%)
# Total Accepted:    3.4K
# Total Submissions: 9.3K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
# 
# 示例:
# 
# 输入: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# 输出: 4
# 
#
class Solution:
    def maximalSquare(self, matrix) -> int:
        # for line in matrix:
        #     print(line)

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        dp_m = [[int(ii) for ii in i] for i in matrix]
        # for line in dp_m:
        #     print(line)
        # print('-----------')
        for i in range(1, len(dp_m)):
            for j in range(1, len(dp_m[0])):
                if dp_m[i][j] == 0:                   
                    pass
                else:
                    if dp_m[i - 1][j - 1] != 0:
                        width = dp_m[i - 1][j - 1]
                        new_width=self.panduan(matrix, width,i,j)
                        if new_width==width:
                            dp_m[i][j] = dp_m[i - 1][j - 1] + 1
                        else:
                            dp_m[i][j]+=new_width
        res = 0
        for line in dp_m:
            res = max(res, max(line))
        return pow(res,2)
    def panduan(self, matrix, width, x, y):
        width_new = 0
        for i in range(width):
            if matrix[x - i - 1][y] == '1' and matrix[x][y - i - 1] == '1':
                width_new += 1
            else:
                break
        return width_new               

if __name__ == '__main__':
    test = Solution()
    a = test.maximalSquare([["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]])
    print(a)

