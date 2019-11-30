#
# @lc app=leetcode.cn id=160 lang=python
#
# [160] 相交链表
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len_heada = self.len_list(headA)
        len_headb = self.len_list(headB)
        if len_heada == 0 or len_headb == 0:
            return
        if len_heada >= len_headb:
            p = headA
            q = headB
        else:
            p = headB
            q = headA
        len_all = max(len_heada, len_headb)
        chazhi = abs(len_heada - len_headb)
        for i in range(1, len_all + 1):
            if id(p) == id(q):
                return p
            p = p.next
            if i > chazhi:
                q = q.next
        return

    def len_list(self, head):
        _len = 0
        while head:
            _len += 1
            head = head.next
        return _len


        

