#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#
# https://leetcode-cn.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (21.79%)
# Total Accepted:    11.7K
# Total Submissions: 53.6K
# Testcase Example:  '"aa"\n"a"'
#
# 给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。
#
# '.' 匹配任意单个字符。
# '*' 匹配零个或多个前面的元素。
#
#
# 匹配应该覆盖整个字符串 (s) ，而不是部分字符串。
#
# 说明:
#
#
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
#
#
# 示例 1:
#
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
#
#
# 示例 2:
#
# 输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: '*' 代表可匹配零个或多个前面的元素, 即可以匹配 'a' 。因此, 重复 'a' 一次, 字符串可变为 "aa"。
#
#
# 示例 3:
#
# 输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个('*')任意字符('.')。
#
#
# 示例 4:
#
# 输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 'c' 可以不被重复, 'a' 可以被重复一次。因此可以匹配字符串 "aab"。
#
#
# 示例 5:
#
# 输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false
#
#
import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        res = re.match(p, s)
        if res and res.span()[1] == len(s):
            return True
        else:
            return False
        #首先把p中以开头的*去掉
        # s_len = len(s)
        # p_len = len(p)
        # if s_len==0:
        #     return
        # if p_len==0:
        #     return False
        # for tem in range(p_len):
        #     if p[tem] != '*':
        #         break
        # if tem == 0:
        #     pass
        # else:
        #     p = p[tem:p_len]
        # s_index = p_index = 0
        # while True:
        #     if p[p_index] == '.' or p[p_index] == s[s_index]:
        #         p_index += 1
        #         s_index += 1
        #     elif p[p_index] == '*':
        #         if p[p_index - 1] == s[s_index]:
        #             s_index += 1
        #         elif p[p_index - 1] == '.':
        #             s_index += 1
        #         else:
        #             p_index+=1
        #     else:
        #         p_index+=1
        #     if s_index == s_len:
        #         return True
        #     if p_index == p_len:
        #         return False
