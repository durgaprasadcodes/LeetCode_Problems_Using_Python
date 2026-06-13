
class Solution:
    def isPalindrome(self, head):

        if not head.next:
            return True
            
        s=f=head
        while f and f.next:
            s=s.next
            f=f.next.next

        prev = s
        curr = s.next
        prev.next = None


        while curr :
            nextNodes = curr.next 
            curr.next = prev
            prev = curr
            curr = nextNodes

        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next

        return True