#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 报数
#
# https://leetcode-cn.com/problems/count-and-say/description/
#
# algorithms
# Easy (48.39%)
# Total Accepted:    22.9K
# Total Submissions: 47.3K
# Testcase Example:  '1'
#
# 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
#
#
# 1 被读作  "one 1"  ("一个一") , 即 11。
# 11 被读作 "two 1s" ("两个一"）, 即 21。
# 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
#
# 给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
#
# 注意：整数顺序将表示为一个字符串。
#
#
#
# 示例 1:
#
# 输入: 1
# 输出: "1"
#
#
# 示例 2:
#
# 输入: 4
# 输出: "1211"
#
#
#


class Solution:
    def tongji(self, zifuchuan):
        mylen = len(zifuchuan)
        jieguo = []
        count = 1
        for i in range(mylen-1):
            if zifuchuan[i] == zifuchuan[i+1]:
                count += 1
            else:
                jieguo.append(str(count))
                jieguo.append(zifuchuan[i])
                count = 1
        jieguo.append(str(count))
        jieguo.append(zifuchuan[mylen-1])
        return jieguo

    def countAndSay(self, n: int) -> str:  
        if n <= 1:
            return "1"
        if n == 2:
            return "11"
        temlist=['1','1']
        for i in range(3,n+1):
            temlist=self.tongji(temlist)
        res=""
        for temm in temlist:
            res=res.__add__(temm)
        return res
        
