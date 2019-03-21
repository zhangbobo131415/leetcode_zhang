#
# @lc app=leetcode.cn id=442 lang=python3
#
# [442] 数组中重复的数据
#
# https://leetcode-cn.com/problems/find-all-duplicates-in-an-array/description/
#
# algorithms
# Medium (59.75%)
# Total Accepted:    3.4K
# Total Submissions: 5.7K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# 给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。
#
# 找到所有出现两次的元素。
#
# 你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？
#
# 示例：
#
#
# 输入:
# [4,3,2,7,8,2,3,1]
#
# 输出:
# [2,3]
#
#
#



class Solution:
    def findDuplicates(self, nums):
        nums_len = nums.__len__()
        reslist = []
        if nums_len == 0:
            return reslist
        for tem in nums:
            if tem < 1 or tem > nums_len:
                return False
        for i in range(nums_len):
            while i != (nums[i] - 1):
                if nums[i] == nums[nums[i] - 1]:#这里很关键不然的话会出现永循环，即对于位置i若数组中不存在大小为i-1的数的时候，这里是循环的出口。
                    break
                else:
                    nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(len(nums)):
            if i != (nums[i] - 1):
                reslist.append(nums[i])
        return reslist
