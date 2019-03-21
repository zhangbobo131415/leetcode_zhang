#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#
# https://leetcode-cn.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (42.73%)
# Total Accepted:    5.7K
# Total Submissions: 13.2K
# Testcase Example:  '"25525511135"'
#
# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
#
# 示例:
#
# 输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"]
#
#
class Solution:
    def __init__(self):
        self.mylist = []

    def hefa(self, s):
        if int(s) <= 255 and str(int(s)) == s:
            return True
        else:
            return False

    def myfunction(self, s, listbiao, cengshu, jieguolist):
        #print(s)
        if len(s) == 0 and cengshu <= 4:
            return
        if cengshu == 4:
            if self.hefa(s):
                listbiao.append(s)
                tem = listbiao.copy()
                jieguolist.append(tem)
                listbiao.pop()
                return
            else:
                return
        for i in range(1, 4):
            if self.hefa(s[0:i]):
                listbiao.append(s[0:i])
                self.myfunction(s[i:s.__len__()], listbiao, cengshu + 1,
                                jieguolist)
                listbiao.pop()
            else:
                return

    def restoreIpAddresses(self, s: str):
        temlist = []
        self.myfunction(s, temlist, 1, self.mylist)
        reslist = []
        for temm in self.mylist:
            reslist.append('.'.join(temm))
        return reslist
