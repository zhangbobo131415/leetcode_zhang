#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#
# https://leetcode-cn.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (60.26%)
# Likes:    274
# Dislikes: 0
# Total Accepted:    20.7K
# Total Submissions: 34K
# Testcase Example:  '[1,3,4,2,2]'
#
# 给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和
# n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
#
# 示例 1:
#
# 输入: [1,3,4,2,2]
# 输出: 2
#
#
# 示例 2:
#
# 输入: [3,1,3,4,2]
# 输出: 3
#
#
# 说明：
#
#
# 不能更改原数组（假设数组是只读的）。
# 只能使用额外的 O(1) 的空间。
# 时间复杂度小于 O(n^2) 。
# 数组中只有一个重复的数字，但它可能不止重复出现一次。
#
#
#


class Solution:
    def findDuplicate(self, nums:list) :
        nums.sort()
        print(nums)
        for index, num in enumerate(nums):
            if num != index + 1:
                return num
        # i = 0
        # j = len(nums) - 1
        # n = len(nums) - 1
        # mid = 0
        # while i < j:
        #     mid = (i + j) // 2
        #     if nums[mid] < n // 2:
        #         j = mid -1
        #     elif nums[mid] > n // 2:
        #         i = mid + 1
        #         if nums[mid] == nums[i]:
        #             return nums[i]
        #     else:
        #         return nums[mid]


if __name__ == '__main__':
    test = Solution()
    a = test.findDuplicate([7,9,7,4,2,8,7,7,1,5])
    print(a)
