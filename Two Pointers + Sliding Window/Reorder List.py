class Solution:
    def reorderList(self, head) -> None:

        if not head or not head.next:
            return

        # find middle
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        curr = slow.next
        slow.next = None

        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # merge two halves
        part1 = head
        part2 = prev
        
        l1=part1
        l2=part2
        
        while l1 and l2 :
            l1_next_node = l1.next
            l2_next_node = l2.next
            
            l1.next=l2
            
            if not l1_next_node:
                break
            l2.next = l1_next_node
            
            l1=l1_next_node
            l2=l2_next_node
        
        return part1
            

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

s=Solution()
print(s.reorderList(head))

# Time Complexity: O(n)
# Space Complexity: O(1)