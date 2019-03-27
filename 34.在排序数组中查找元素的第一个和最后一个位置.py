#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (35.45%)
# Total Accepted:    13.8K
# Total Submissions: 38.9K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 如果数组中不存在目标值，返回 [-1, -1]。
#
# 示例 1:
#
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
#
# 示例 2:
#
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]
#
#
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        len_nums = len(nums)
        i = 0
        j = len_nums - 1
        mid = (i + j) // 2
        res = []
        while i <= j:
            if nums[mid] == target:
                for i in range(i, j + 1):
                    if nums[i] == target:
                        res.append(i)
                break
            elif nums[mid] < target:
                i = mid + 1
                mid = (i + j) // 2
            else:
                j = mid - 1
                mid = (i + j) // 2
        if res.__len__() == 0:
            return [-1, -1]
        real_res = [res[0], res[-1]]
        return real_res
