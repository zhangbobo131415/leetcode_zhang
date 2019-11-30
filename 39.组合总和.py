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

# def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#     if min(candidates) <= 0 or target <= 0:
#         return
#     len_candidates = len(candidates)
#     tem_list = []
#     res_list = []
#     sum_ = 0
#     self.backtrack(candidates, 0, target, len_candidates, sum_, tem_list,
#                     res_list)
#     return res_list

# def backtrack(self, candidates, start_index, target, len_candidates, sum_,
#                 tem_list, res_list):
#     if sum_ == target:
#         res_list.append(tem_list.copy())
#         return
#     if sum_ > target:
#         return
#     for i in range(start_index, len_candidates):
#         tem_list.append(candidates[i])
#         self.backtrack(candidates, start_index, target, len_candidates,
#                         sum_ + candidates[i], tem_list, res_list)
#         tem_list.pop()




class Solution:
    target = int(input())
    def combinationSum(self, target):
        
        candidates = data = [i+1 for i in range(target)]
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
            tem.append(candidates[i])
            # 剪枝加速运算
            if sum_ + candidates[i] > target:
                tem.pop(-1)
                break
            # 在解空间搜索的时候可以只遍历子节点大于等于父节点的节点这样可以有效消除重复解
            # 例如在本例中，5为父节点时，子节点只能为5、7。3为父节点时，子节点只能是3、5、7
            # 这样可以去重
            self.backtrack(candidates, target, i, tem, res, sum_ + candidates[i])
            tem.pop(-1)
        return


if __name__ == '__main__':
    test = Solution()
    data = [i+1 for i in range(10)]
    a = test.combinationSum(data, 10)
    for i in a:
        print(i)