#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __lt__(self, ex):
        return self.val<ex.val
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        tem_heap = []
        for i in lists:
            if i:
                tem_heap.append(i)
        heapq.heapify(tem_heap)
        print(tem_heap)
        # res = ListNode(0)
        # while len(tem_heap)>0:
        #     if tem_heap[0].next:
        #         _, res.next = heapq.heappushpop(tem_heap,(tem_heap[0].next.val,tem_heap[0].next))
        #     else:
        #         _, res.next = heapq.heappop(tem_heap)
        # print(res)
        
        
        
                
        

