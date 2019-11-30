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
    def combinationSum2(self, candidates, target: int) :
        res = []
        tem = []
        candidates.sort()
        self.backtrack(candidates, target, 0, tem, res, 0)
        return res
    def backtrack(self, candidates, target, start_index, tem, res, sum_):
        if sum_ == target:
            res.append(tem.copy())
            return
        for i in range(start_index, len(candidates)):
            if i > start_index:
                if candidates[i] == candidates[i - 1]:
                    continue
            tem.append(candidates[i])
            # 剪枝加速运算
            if sum_ + candidates[i] > target:
                tem.pop(-1)
                break
            # 在解空间搜索的时候可以只遍历子节点大于等于父节点的节点这样可以有效消除重复解
            # 例如在本例中，5为父节点时，子节点只能为5、7。3为父节点时，子节点只能是3、5、7
            # 这样可以去重
            self.backtrack(candidates, target, i + 1, tem, res, sum_ + candidates[i])
            tem.pop(-1)
        return
if __name__ == '__main__':
    test = Solution()
    a = test.combinationSum2([10,1,2,7,6,1,5], 8)
    print(a)

    #     if min(candidates) <= 0 or target <= 0:
    #         return
    #     len_candidates = len(candidates)
    #     tem_list = []
    #     res_list = []
    #     sum_ = 0
    #     self.backtrack(candidates, 0, target, len_candidates, sum_, tem_list,
    #                    res_list)
    #     return res_list

    # def backtrack(self, candidates, start_index, target, len_candidates, sum_,
    #               tem_list, res_list):
    #     if sum_ == target:
    #         res_list.append(tem_list.copy())
    #         return
    #     if sum_ > target:
    #         return
    #     for i in range(start_index, len_candidates):
    #         tem_list.append(candidates[i])
    #         self.backtrack(candidates, i + 1, target, len_candidates,
    #                        sum_ + candidates[i], tem_list, res_list)
    #         tem_list.pop()
