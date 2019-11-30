#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#
class Solution:
    def firstUniqChar(self, s: str) -> int:
        tem_dict = {}
        for i in s:
            if i in tem_dict:
                tem_dict[i] += 1
            else:
                tem_dict[i] = 1
        for index,i in enumerate(s):
            if tem_dict[i] == 1:
                return index
        return -1
        

