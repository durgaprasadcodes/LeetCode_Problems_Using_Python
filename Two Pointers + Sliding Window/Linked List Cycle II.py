class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow=fast=head
        c=0
        while fast and fast.next:

            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                c=1
                break

        if c!=1:
            return None
        
        start=head

        while start!=slow:
            start=start.next
            slow=slow.next

        return slow