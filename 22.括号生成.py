#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (70.99%)
# Likes:    512
# Dislikes: 0
# Total Accepted:    39.9K
# Total Submissions: 55.6K
# Testcase Example:  '3'
#
# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
#
#
#


class Solution:
    def generateParenthesis(self, n: int):
        res = []
        stack = ''
        self.backtrack(0, 0, stack, res, n)
        return res

    def backtrack(self, lef, right, canshu_stack, res, n):
        stack = canshu_stack[:]
        if lef == n:
            stack = stack+(')' * (n-right))
            res.append(stack)
            return
        if lef > right:
            stack = stack+('(')
            self.backtrack(lef + 1, right, stack, res, n)
            stack = stack[0:-1]
            stack = stack+(')')
            self.backtrack(lef, right + 1, stack, res, n)
            stack = stack[0:-1]
        elif lef == right:
            stack = stack+('(')
            self.backtrack(lef + 1, right, stack, res, n)
            stack = stack[0:-1]
        else:
            pass
        return


if __name__ == '__main__':
    test = Solution()
    data = 4
    res = test.generateParenthesis(data)
    print(res)
