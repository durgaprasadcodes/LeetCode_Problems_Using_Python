
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head:
            return head
        old_head = head
        nodes = {None: None}
        while old_head:
            nodes[old_head] = Node(old_head.val)
            old_head = old_head.next
        old_head = head
        while old_head:
            nodes[old_head].next = nodes[old_head.next]
            nodes[old_head].random = nodes[old_head.random]
            old_head = old_head.next
        return nodes[head]