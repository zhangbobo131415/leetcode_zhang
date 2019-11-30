#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#
# https://leetcode-cn.com/problems/largest-number/description/
#
# algorithms
# Medium (32.75%)
# Likes:    141
# Dislikes: 0
# Total Accepted:    10.3K
# Total Submissions: 30.8K
# Testcase Example:  '[10,2]'
#
# 给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。
# 
# 示例 1:
# 
# 输入: [10,2]
# 输出: 210
# 
# 示例 2:
# 
# 输入: [3,30,34,5,9]
# 输出: 9534330
# 
# 说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。
# 
#
import functools
class Solution:
    
    def cmp_(self, x, y):
        tem1, tem2 = x + y, y + x
        if tem1 < tem2:
            return 1
        else:
            return -1
        
    def largestNumber(self, nums) -> str:
        if sum(nums) == 0:
            return '0'
        str_nums = [str(i) for i in nums]
        str_nums.sort(key=functools.cmp_to_key(self.cmp_))
        res = ''    
        for i in str_nums:
            res += i
        return res
if __name__ == '__main__':
    test = Solution()
    test.largestNumber([3, 32, 34, 5, 9])
    print(functools.cmp_to_key(test.cmp_)('a'))

