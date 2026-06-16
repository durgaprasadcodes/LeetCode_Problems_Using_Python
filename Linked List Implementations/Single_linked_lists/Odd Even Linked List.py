class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head):

        if not head or not head.next:
            return head
        # ========= 1 ===========
        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head

        return head
        
        #  ========= 2 ===========
        # ODD = ListNode(0)
        # EVEN = ListNode(0)
        # odd = ODD
        # even = EVEN
        # curr = head
        # is_even = False
        # while curr:
        #     if is_even :
        #         is_even = False
        #         even.next = curr
        #         even = even.next
        #     else:
        #         is_even = True
        #         odd.next = curr
        #         odd = odd.next
        #     curr = curr.next
        # odd.next = EVEN.next
        # even.next = None

        # return ODD.next