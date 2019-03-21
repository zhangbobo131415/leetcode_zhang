#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
# https://leetcode-cn.com/problems/add-binary/description/
#
# algorithms
# Easy (46.80%)
# Total Accepted:    18.1K
# Total Submissions: 38.6K
# Testcase Example:  '"11"\n"1"'
#
# 给定两个二进制字符串，返回他们的和（用二进制表示）。
#
# 输入为非空字符串且只包含数字 1 和 0。
#
# 示例 1:
#
# 输入: a = "11", b = "1"
# 输出: "100"
#
# 示例 2:
#
# 输入: a = "1010", b = "1011"
# 输出: "10101"
#
#
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aoflen = a.__len__()
        boflen = b.__len__()

        maxlen = max(aoflen, boflen) + 1
        res = ""
        temres = [0] * maxlen
        jinwei = 0
        alist = []
        blist = []
        for i in range(maxlen):
            if i < aoflen:
                alist.insert(0, a[i])
            else:
                alist.append("0")
            if i < boflen:
                blist.insert(0, b[i])
            else:
                blist.append("0")

        for i in range(maxlen):
            temres[i] = int((int(alist[i]) + int(blist[i]) + jinwei) % 2)
            jinwei = int((int(alist[i]) + int(blist[i]) + jinwei) / 2)
        temres.reverse()
        for i in range(maxlen):
            if i == 0 and temres[i] == 0:
                pass
            else:
                res = res.__add__(str(temres[i]))
        return res
