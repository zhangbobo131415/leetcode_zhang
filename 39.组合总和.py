#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
# https://leetcode-cn.com/problems/combination-sum/description/
#
# algorithms
# Medium (63.16%)
# Total Accepted:    13.7K
# Total Submissions: 21.7K
# Testcase Example:  '[2,3,6,7]\n7'
#
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的数字可以无限制重复被选取。
#
# 说明：
#
#
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。
#
#
# 示例 1:
#
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
#
#
# 示例 2:
#
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
#
#
class Solution:
    def backtrack(self, candidates, start_index, target, len_candidates, sum_,
                  tem_list, res_list):
        if sum_ == target:
            res_list.append(tem_list.copy())
            return
        if sum_ > target:
            return
        for i in range(start_index, len_candidates):
            tem_list.append(candidates[i])
            self.backtrack(candidates, start_index, target, len_candidates,
                           sum_ + candidates[i], tem_list, res_list)
            tem_list.pop()

    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:
        if min(candidates) <= 0 or target <= 0:
            return
        len_candidates = len(candidates)
        tem_list = []
        res_list = []
        sum_ = 0
        self.backtrack(candidates, 0, target, len_candidates, sum_, tem_list,
                       res_list)
        return res_list
