#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (48.12%)
# Total Accepted:    18.6K
# Total Submissions: 38.6K
# Testcase Example:  '"23"'
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
#
#
# 示例:
#
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
#
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
#
#
class Solution:
    def backtrack(self, digits, start_index, len_digits, res_stack,
                  yingshe_dic, tem_stack):
        if start_index == len_digits:
            tem_str = ""
            for j in tem_stack:
                tem_str += j
            res_stack.append(tem_str)
            return
        for tem in range(len(yingshe_dic[digits[start_index]])):
            tem_stack.append(yingshe_dic[digits[start_index]][tem])
            self.backtrack(digits, start_index + 1, len_digits, res_stack,
                           yingshe_dic, tem_stack)
            tem_stack.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        yingshe_dic = {}
        yingshe_dic['2'] = ['a', 'b', 'c']
        yingshe_dic['3'] = ['d', 'e', 'f']
        yingshe_dic['4'] = ['g', 'h', 'i']
        yingshe_dic['5'] = ['j', 'k', 'l']
        yingshe_dic['6'] = ['m', 'n', 'o']
        yingshe_dic['7'] = ['p', 'q', 'r', 's']
        yingshe_dic['8'] = ['t', 'u', 'v']
        yingshe_dic['9'] = ['w', 'x', 'y', 'z']
        len_digits = len(digits)
        for i in range(len_digits):
            if digits[i] not in yingshe_dic:
                return
        tem_stack = []
        res_stack = []
        if len_digits == 0:
            return res_stack
        self.backtrack(digits, 0, len_digits, res_stack, yingshe_dic,
                       tem_stack)
        return res_stack
