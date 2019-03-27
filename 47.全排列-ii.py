#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
# https://leetcode-cn.com/problems/permutations-ii/description/
#
# algorithms
# Medium (51.15%)
# Total Accepted:    8.6K
# Total Submissions: 16.9K
# Testcase Example:  '[1,1,2]'
#
# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
#
# 示例:
#
# 输入: [1,1,2]
# 输出:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
#
#
class Solution:
    def permuteUnique(self, nums):
        res = []
        maxlist = []
        nums.sort()
        res.append(nums.copy())
        maxlist = nums.copy()
        maxlist.sort(reverse=True)
        while nums != maxlist:
            self.nextPermutation(nums)
            res.append(nums.copy())
        return res

    def nextPermutation(self, nums) -> None:
        # maxtem = nums.copy()
        # maxtem.sort(reverse=True)
        # if maxtem == nums:
        #     nums.sort()
        # else:
        for i in range(nums.__len__() - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                qianzhuilist = nums[0:i - 1]
                houzhuilist = nums[i - 1:nums.__len__()]
                houzhuilist.sort(reverse=True)
                weizhi = houzhuilist.index(nums[i - 1])
                qianzhuilist.append(houzhuilist.pop(weizhi - 1))
                houzhuilist.sort()
                qianzhuilist.extend(houzhuilist)
                for maxlist in range(qianzhuilist.__len__()):
                    nums[maxlist] = qianzhuilist[maxlist]
                break
                    
                    
