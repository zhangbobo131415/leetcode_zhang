#
# @lc app=leetcode.cn id=946 lang=python3
#
# [946] 验证栈序列
#


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        tem_stack = []
        index_pop = 0
        if len(pushed) == 0:
            return True
        for i in pushed:
            tem_stack.append(i)
            while len(tem_stack) > 0 and tem_stack[-1] == popped[index_pop]:
                tem_stack.pop()
                index_pop += 1
        if len(tem_stack) != 0:
            return False
        else:
            return True
