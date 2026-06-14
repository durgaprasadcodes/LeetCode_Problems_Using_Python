
class Solution:
    def pairSum(self, head): 
        if not head.next:
            return head.val
        if not head.next.next:
            return head.val + head.next.val

        s=f=head

        while f and f.next:
            s=s.next
            f=f.next.next

        prev=s
        curr=s.next
        prev.next=None

        while curr:
            nextNodes = curr.next
            curr.next = prev
            prev = curr
            curr = nextNodes

        max_sum = 0

        print(max_sum,head.val + prev.val)

        while prev:
            curr_sum = head.val + prev.val
            max_sum = max_sum if curr_sum < max_sum else curr_sum
            head = head.next
            prev = prev.next

        return max_sum