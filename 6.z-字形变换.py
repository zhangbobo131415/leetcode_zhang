#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#
# https://leetcode-cn.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (43.66%)
# Likes:    396
# Dislikes: 0
# Total Accepted:    57.8K
# Total Submissions: 128.7K
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
#
# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
#
# L   C   I   R
# E T O E S I I G
# E   D   H   N
#
#
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
#
# 请你实现这个将字符串进行指定行数变换的函数：
#
# string convert(string s, int numRows);
#
# 示例 1:
#
# 输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"
#
#
# 示例 2:
#
# 输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
# 解释:
#
# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G
#
#


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        tem = ["" for i in range(numRows)]
        res = ''
        currrow = 0
        chang_fangxiang = False
        if numRows == 1:
            return s 
        
        for item in s:
            if currrow == 0 or currrow == numRows - 1:
                chang_fangxiang = not chang_fangxiang
            if chang_fangxiang == True:
                step = 1
            else:
                step = -1
            tem[currrow]+=item
            currrow +=step
        for k in tem:
            res += k
        return res 



        # res = ''
        # length = len(s)
        # if numRows == 1:
        #     return s 
        # tem = [[None for i in range(length // (2*numRows-1) *numRows+ 1)]
        #        for k in range(numRows)]
        # i = j = k = 0
        # while True:
        #     if i == 0:
        #         for m in range(numRows):
        #             if k >= length:
        #                 break
        #             tem[i][j] = s[k]
        #             i += 1
        #             k += 1
        #         if k >= length:
        #                 break
        #         i -= 1
        #         k-=1
        #     elif i == numRows - 1:
        #         for m in range(numRows):
        #             if k >= length:
        #                 break
        #             tem[i][j] = s[k]
        #             i -= 1
        #             j += 1
        #             k += 1
        #         if k >= length:
        #             break
        #         i += 1
        #         j -= 1
        #         k -= 1
        # for i in tem:
        #     for k in i:
        #         if k != None:
        #             res += k
                    
            
        # return res

        # res =''
        # length = len(s)
        # for i in range(numRows):
        #     k = i
        #     while k < length:
        #         res += s[k]
        #         k += (numRows - i - 1) * 2



if __name__ == '__main__':
    test = Solution()
    a = test.convert("abcd", 3)
    print(a)
    # for i in a:
    #     print(i)
