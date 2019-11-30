class Solution(object):
    def hasCycle(self, head)->bool:
        """
        :type head: ListNode
        :rtype: bool
        """
        p = head
        if p == None:
            return False
        q = head.next
        if q == None:
            return False
        if q == p:
            return True
        while p != q:
            p = p.next
            if q.next != None and q.next.next != None:
                q = q.next.next
            else:
                return False
            if p == q:
                return True
            
