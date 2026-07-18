class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        def merge(l1,l2):
            dummy = ListNode(0)
            head = dummy
            while l1 and l2 :
                if l1.val <= l2.val:
                    head.next = l1
                    l1 = l1.next
                else:
                    head.next = l2
                    l2 = l2.next
                head = head.next
            if l1:
                head.next = l1
            if l2:
                head.next = l2
            return dummy.next
            
        def devide(lists,l,r):
            mid = (l+r)//2
            if l == r:
                return lists[l]
            l1 = devide(lists,l,mid)
            l2 = devide(lists,mid+1,r)
            return merge(l1,l2)

        return devide(lists,0,len(lists)-1)
