#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (24.81%)
# Total Accepted:    44.3K
# Total Submissions: 178.6K
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#
#
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"
#
#
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        lenofs = len(s)
        if lenofs == 0:
            return ""
        tem_res = [0 for i in self.dingyihanshu(0, lenofs, 0.5)]
        mid = [i for i in self.dingyihanshu(0, lenofs, 0.5)]
        temmm = s[0]
        for i in s:
            if i != temmm:
                break
        if i == lenofs - 1:
            return s
        for j in mid:
            if int(j) == j:
                j = int(j)
                for k in range(1, j + 1):
                    if j + k <= lenofs - 1 and s[j + k] == s[j - k]:
                        tem_res[j * 2] += 2
                    else:
                        break
                tem_res[j * 2] += 1
            else:
                for k in range(int(j), -1, -1):
                    if int(j * 2 - k) <= lenofs - 1 and s[k] == s[int(j * 2 -
                                                                      k)]:
                        tem_res[int(j * 2)] += 2
                    else:
                        break
        maxlen = max(tem_res)
        index = tem_res.index(maxlen)
        if mid[index] == int(mid[index]):
            return s[int(mid[index]) - maxlen // 2:int(mid[index]) +
                     maxlen // 2 + 1]
        else:
            return s[int(mid[index]) - maxlen // 2 + 1:int(mid[index]) +
                     maxlen // 2 + 1]

    def dingyihanshu(self, start, end, step):
        end = end - 1
        while start <= end:
            yield start
            start = start + step
