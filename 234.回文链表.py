#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
# https://leetcode-cn.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (35.68%)
# Total Accepted:    18.8K
# Total Submissions: 52.6K
# Testcase Example:  '[1,2]'
#
# 请判断一个链表是否为回文链表。
#
# 示例 1:
#
# 输入: 1->2
# 输出: false
#
# 示例 2:
#
# 输入: 1->2->2->1
# 输出: true
#
#
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#从mid+1开始将链表反转，然后依次判断是否相同即可
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        lenhead = 0
        tem = head
        mid = head
        while tem:
            lenhead += 1
            if lenhead & 1 == 1 and lenhead > 2:
                mid = mid.next
            if tem.next == None:
                break
            tem = tem.next
        if lenhead == 0:
            return True
        if lenhead & 1 == 0:
            mid = mid.next
        head2 = self.reverselist(mid)
        while head and head2:
            if head.val != head2.val:
                return False
            head, head2 = head.next, head2.next
        return True

    def reverselist(self, head):
        p = head.next
        if p == None:
            return head
        q = p.next
        head.next = None
        while p:
            p.next, head = head, p
            if q == None:
                return p
            p, q = q, q.next
