#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#
# https://leetcode-cn.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (33.86%)
# Likes:    131
# Dislikes: 0
# Total Accepted:    11.5K
# Total Submissions: 33.2K
# Testcase Example:  '[2,3,2]'
#
# 
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
# 
# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
# 
# 示例 1:
# 
# 输入: [2,3,2]
# 输出: 3
# 解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
# 
# 
# 示例 2:
# 
# 输入: [1,2,3,1]
# 输出: 4
# 解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
# 偷窃到的最高金额 = 1 + 3 = 4 。
# 
#
class Solution:
    def rob(self, nums: list) -> int:
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        if length == 2:
            return 0
        pre_pre = 0
        pre = 0
        current = 0
        for index, num in enumerate(nums):
            if index ==0 :
                continue
            current = max(pre_pre + num, pre)
            pre_pre =pre
            pre = current
        pre_pre = 0
        pre = 0
        current_2 = 0
        for index, num in enumerate(nums):
            if index ==length - 1 :
                continue
            current_2 = max(pre_pre + num, pre)
            pre_pre =pre
            pre = current_2    
        return max(current_2,current)  

