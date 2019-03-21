#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (32.01%)
# Total Accepted:    97.2K
# Total Submissions: 303.7K
# Testcase Example:  '123'
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 
# 示例 1:
# 
# 输入: 123
# 输出: 321
# 
# 
# 示例 2:
# 
# 输入: -123
# 输出: -321
# 
# 
# 示例 3:
# 
# 输入: 120
# 输出: 21
# 
# 
# 注意:
# 
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
# 
#
class Solution:
    def reverse(self, x: int) -> int:
        fanwei=[-pow(2,31),pow(2,31)-1]
        tem=abs(x)
        resversnum=0
        while tem:
            resversnum=resversnum*10+tem%10
            tem=int(tem/10)
            if resversnum<fanwei[0] or resversnum>fanwei[1]:
                return 0
        if x<0:
            resversnum=-1*resversnum
        return resversnum


        

