class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):

        # l1 = headA
        # l2 = headB

        # while l1 is not l2:
        #     l1 = l1.next if l1 else headB
        #     l2 = l2.next if l2 else headA
        # return l1

        l1_len = l2_len = 0
        l1 = headA
        l2 = headB
        while l1 or l2 :
            l1_len = l1_len + 1 if l1 else l1_len
            l2_len = l2_len + 1 if l2 else l2_len
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if l1_len > l2_len:
            big = headA
            small = headB
            max_len = l1_len
            min_len = l2_len
        else:
            small = headA
            big = headB
            max_len = l2_len
            min_len = l1_len
        diff = max_len-min_len
        for _ in range(diff):
            big = big.next
        while big and small:
            if big is small:
                return big
            big = big.next
            small = small.next
        return None