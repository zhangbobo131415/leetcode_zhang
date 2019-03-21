#
# @lc app=leetcode.cn id=862 lang=python3
#
# [862] 字符串中的查找与替换
#
# https://leetcode-cn.com/problems/shortest-subarray-with-sum-at-least-k/description/
#
# algorithms
# Hard (9.57%)
# Total Accepted:    1K
# Total Submissions: 10.7K
# Testcase Example:  '[1]\n1'
#
# 返回 A 的最短的非空连续子数组的长度，该子数组的和至少为 K 。
# 
# 如果没有和至少为 K 的非空子数组，返回 -1 。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：A = [1], K = 1
# 输出：1
# 
# 
# 示例 2：
# 
# 输入：A = [1,2], K = 4
# 输出：-1
# 
# 
# 示例 3：
# 
# 输入：A = [2,-1,2], K = 3
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 50000
# -10 ^ 5 <= A[i] <= 10 ^ 5
# 1 <= K <= 10 ^ 9
# 
# 
#
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        

