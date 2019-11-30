#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
class Solution:
    def isValid(self, s: str) -> bool:
        tem_stack = []
        zuo_kuohao = set(['(', '[', '{'])
        you_kuohao = dict(zip([')', ']', '}'],['(', '[', '{']))
        s_len = len(s)
        if s_len == 0:
            return True
        if s[0] not in zuo_kuohao:
            return False
        tem_stack.append(s[0])
        for i in range(1, s_len):
            if s[i] in zuo_kuohao:
                tem_stack.append(s[i])
            elif s[i] in you_kuohao:
                if len(tem_stack)>0 and you_kuohao[s[i]] == tem_stack[-1]:
                    tem_stack.pop()
                else:
                    return False
            else:
                return False
        if len(tem_stack) != 0:
            return False
        else:
            return True       
