class Solution:
    def flatten(self, head):
        stack=[]
        cur = head
        while cur:
            if cur.child:
                if cur.next:
                    stack.append(cur.next)
                cur.next=cur.child
                cur.child.prev=cur
                cur.child=None
            if not cur.next and stack:
                nxt = stack.pop()
                cur.next=nxt
                nxt.prev=cur
            cur=cur.next
        return head
