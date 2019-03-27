#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子序列
#
# https://leetcode-cn.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (32.88%)
# Total Accepted:    6.5K
# Total Submissions: 19.9K
# Testcase Example:  '[2,3,-2,4]'
#
# 给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
#
# 示例 1:
#
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#
#
# 示例 2:
#
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
#
#


#leetcode 152 因为i可能负整数，因此以i-1结尾的最小数与i的积可能最大，因此需要用两个额外的数组来保存以i为结束元素的最大值与最小值
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        len_nums = len(nums)
        if len_nums == 0:
            return
        if len_nums == 1:
            return nums[0]
        max_list = [0 for i in range(len_nums)]
        min_list = [0 for i in range(len_nums)]
        max_num = min_list[0] = max_list[0] = nums[0]

        for i in range(1, len_nums):
            max_list[i] = max(max_list[i - 1] * nums[i], nums[i],
                              min_list[i - 1] * nums[i])
            min_list[i] = min(min_list[i - 1] * nums[i], nums[i],
                              max_list[i - 1] * nums[i])
            max_num = max(max_list[i], min_list[i], max_num)
        return max_num
