#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
# https://leetcode-cn.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (54.10%)
# Total Accepted:    9.7K
# Total Submissions: 17.9K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的每个数字在每个组合中只能使用一次。
#
# 说明：
#
#
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。
#
#
# 示例 1:
#
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
#
#
# 示例 2:
#
# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
# [1,2,2],
# [5]
# ]
#
#
class Solution:
    def combinationSum2(self, candidates: List[int],
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

    def backtrack(self, candidates, start_index, target, len_candidates, sum_,
                  tem_list, res_list):
        if sum_ == target:
            res_list.append(tem_list.copy())
            return
        if sum_ > target:
            return
        for i in range(start_index, len_candidates):
            tem_list.append(candidates[i])
            self.backtrack(candidates, i + 1, target, len_candidates,
                           sum_ + candidates[i], tem_list, res_list)
            tem_list.pop()
