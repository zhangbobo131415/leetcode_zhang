#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
# https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Easy (38.24%)
# Likes:    172
# Dislikes: 0
# Total Accepted:    11.2K
# Total Submissions: 29.1K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
# 
# 字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
# 
# 说明：
# 
# 
# 字母异位词指字母相同，但排列不同的字符串。
# 不考虑答案输出的顺序。
# 
# 
# 示例 1:
# 
# 
# 输入:
# s: "cbaebabacd" p: "abc"
# 
# 输出:
# [0, 6]
# 
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
# 
# 
# 示例 2:
# 
# 
# 输入:
# s: "abab" p: "ab"
# 
# 输出:
# [0, 1, 2]
# 
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
# 
# 
#

# sub是s的子串且与p等长；令tmp = sub-p；减号的意思为sub与p中各个字符出现的次数的差；
class Solution:
    def findAnagrams(self, s: str, p: str):
        res=[]
        tmp = {}
        length = len(p)
        # 初始时sub为"",所以tmp中key对应的value均为负值
        for i in p:
            if i in tmp:
                tmp[i] -= 1
            else:
                tmp[i] = -1
        tmp2 = set(p)

        for index, i in enumerate(s):
            # index >= length时需要从sub的左侧去掉一个字符即s[index - length]
            if index >= length:
                # 判断s[index - length]是否时p中的字符
                if s[index - length] in tmp2:
                    if s[index - length] in tmp:
                        # 如果s[index - length]出现在差tmp中,因为要去掉s[index - length]，所以tmp[s[index - length]] -= 1
                        tmp[s[index - length]] -= 1
                        if tmp[s[index - length]] == 0:
                            tmp.pop(s[index - length])
                    else:
                        # 否则，直接让tmp[s[index - length]] = -1
                        tmp[s[index - length]] = -1
                else:
                    tmp.pop(s[index - length])
            
            # sub的右侧添加一个字符
            if i in tmp:
                tmp[i] += 1
                if tmp[i] == 0:
                    tmp.pop(i)
            else:
                tmp[i] = 1

        
            # print(index-length)
            if len(tmp) == 0:
                res.append(index - length + 1)
        return res


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        fuzhu_dic = {s[0]:0}
        changdu = 1
        left =0
        for i in range(1, len(s)):
            if s[i] not in fuzhu_dic:
                fuzhu_dic[s[i]] = i
                changdu=max(changdu,len(fuzhu_dic))
            else:
                end_weizhi = fuzhu_dic[s[i]]
                start_weizhi = left
                left = end_weizhi +1
                fuzhu_dic[s[i]] = i
                for tem in range(start_weizhi, end_weizhi):
                    fuzhu_dic.pop(s[tem])
        return changdu               
            
if __name__ == "__main__":
    test = Solution()
    res = test.findAnagrams("cbaebabacd", "abc")
    print(res)
            
        

