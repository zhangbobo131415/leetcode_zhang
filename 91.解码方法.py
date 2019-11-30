#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#
# https://leetcode-cn.com/problems/decode-ways/description/
#
# algorithms
# Medium (19.95%)
# Total Accepted:    5.2K
# Total Submissions: 26.2K
# Testcase Example:  '"12"'
#
# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。
# 
# 示例 1:
# 
# 输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
# 
# 
# 示例 2:
# 
# 输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
# 
# 
#
class Solution:
    def numDecodings(self, s: str) -> int:
        res = [0]
        len_s = len(s)
        tem_index = 0
        while tem_index != -1:
            tem_index = s.find('0', tem_index)
            if tem_index != -1:
                if tem_index == 0:
                    return res[0]
                else:
                    if s[tem_index - 1] == '1' or s[tem_index - 1] == '2':
                        pass
                    else:
                        return res[0]


        self.backtrack(0, s, res, len_s)
        return res[0]
    def backtrack(self, index: int, s: str, res: list, len_s):
        if index == len_s:
            res[0] += 1
            return
        if index > len_s:
            return
        if 1 <= int(s[index:index + 1]) <= 26:
            self.backtrack(index + 1, s, res, len_s)
        if 1 <= int(s[index:index + 2]) <= 26:
            self.backtrack(index + 2, s, res, len_s)
        else:
            return
        return
        
