#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        res = res_tail = Node(0,None,None)
        tem = head
        dict_tem = {}
        while head:
            res_tail.next = Node(head.val,None,None)
            res_tail = res_tail.next
            dict_tem[head] = res_tail
            head = head.next
        res = res.next
        res_tail = res  
        head = tem
        while head:
            if head.random:
                res.random = dict_tem[head.random]
            head, res = head.next, res.next
        res = res_tail
        dict_tem.clear()
        return res
