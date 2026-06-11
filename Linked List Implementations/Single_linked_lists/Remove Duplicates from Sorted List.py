class Solution:
    def deleteDuplicates(self, head):
        if head == None:
            return head
        if head and head.next == None:
            return head

        prev = head 
        curr = head.next
        while curr:
            if prev.val==curr.val:
                prev.next=curr.next
            else:
                prev=curr
            curr=curr.next
        return head