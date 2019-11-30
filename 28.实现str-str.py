#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现strStr()
#
# https://leetcode-cn.com/problems/implement-strstr/description/
#
# algorithms
# Easy (38.03%)
# Total Accepted:    44.3K
# Total Submissions: 116.7K
# Testcase Example:  '"hello"\n"ll"'
#
# 实现 strStr() 函数。
#
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置
# (从0开始)。如果不存在，则返回  -1。
#
# 示例 1:
#
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
#
#
# 示例 2:
#
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
#
#
# 说明:
#
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
#
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
#
#


#重新学习KMP算法：
#最重要的是去求模式的next数组，即前缀后缀最长公共元素长度
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_haystack = len(haystack)
        len_needle = len(needle)
        next = [0 for i in range(len_needle)]
        if len_needle == 0:
            return 0
        for i in range(1, len_needle):
            if needle[i] == needle[next[i - 1]]:
                next[i] = next[i - 1] + 1
            else:
                temmm = next[i - 1] - 1
                while temmm >= 0:+
                    if needle[i] == needle[next[temmm]]:
                        next[i] = next[temmm] + 1
                        break
                    temmm = next[temmm] - 1
        next.insert(0, -1)
        next.pop()
        haindex = neindex = 0
        while haindex < len_haystack:
            if haystack[haindex] == needle[neindex]:
                haindex, neindex = haindex + 1, neindex + 1
            else:
                if neindex == 0:
                    haindex += 1
                else:
                    neindex = next[neindex]
            if neindex == len_needle:
                return haindex - neindex
        return -1
