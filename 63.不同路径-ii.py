#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#
# https://leetcode-cn.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (31.65%)
# Likes:    167
# Dislikes: 0
# Total Accepted:    23.1K
# Total Submissions: 72.7K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
# 
# 
# 
# 网格中的障碍物和空位置分别用 1 和 0 来表示。
# 
# 说明：m 和 n 的值均不超过 100。
# 
# 示例 1:
# 
# 输入:
# [
# [0,0,0],
# [0,1,0],
# [0,0,0]
# ]
# 输出: 2
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
# 
# 
#


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        dp = [i.copy() for i in obstacleGrid]
        m = len(obstacleGrid)
        if m > 0:    
            n = len(obstacleGrid[0])
        else:
            n = 0
            return 0
        dp[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1,m):
            if obstacleGrid[i][0]==0:
                dp[i][0] = dp[i-1][0]
            else:
                dp[i][0] = 0

        for i in range(1,n):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = dp[0][i-1]
            else:
                dp[0][i] = 0

        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
if __name__ == '__main__':
    test = Solution()
    a = test.uniquePathsWithObstacles([[1,0]])
    print(a)  
        
