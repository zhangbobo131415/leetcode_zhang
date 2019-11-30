#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
# https://leetcode-cn.com/problems/group-anagrams/description/
#
# algorithms
# Medium (54.67%)
# Total Accepted:    13.2K
# Total Submissions: 24.1K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
#
# 示例:
#
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
# 输出:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
#
# 说明：
#
#
# 所有输入均为小写字母。
# 不考虑答案输出的顺序。
#
#
#


#关键时去寻找一个映射，一个将有相同字母组成的单词映射为同一个值的映射。
#最好的解决办法时寻找26个质数，然后求每个字符串的积，并用hash存储
#这里主要是将字符串专为列表，然后进行字典排序，这样具有相同字母组成的字符串就对应同一个列表了
class Solution:
    def groupAnagrams(self, strs):
        strslen = strs.__len__()
        res = []
        #tem用来存放字典排序后的列表
        tem = []
        if strslen <= 0:
            return []
        for i in range(0, strslen):
            # tem_root=self.str_to_list(strs[i])
            # tem_root.sort()
            tem_root = sorted(strs[i])
            #判断当前字符串的字典排序列表是否存在于tem中
            if tem_root in tem:
                index_root = tem.index(tem_root)
                res[index_root].append(strs[i])
            else:
                #否则tem和res均append一下
                res.append([strs[i]])
                tem.append(tem_root)
        print(res)
        return res

    def str_to_list(self, strs):
        res = []
        for i in range(len(strs)):
            res.append(strs[i])
        return res
