class Solution:
    def nodesBetweenCriticalPoints(self, head):
        if not head.next.next:
            return [-1,-1]

        prev = head
        slow = head.next
        fast = head.next.next
        criticalPoint   = []
        idx = 2
        while fast:
            if slow.val < prev.val and slow.val < fast.val:
                criticalPoint .append(idx)
            elif slow.val > prev.val and slow.val > fast.val:
                criticalPoint .append(idx)
            idx+=1
            prev = prev.next
            slow = slow.next
            fast = fast.next

        if len(criticalPoint )<=1:
            return [-1,-1]
        maximum = criticalPoint[-1] - criticalPoint[0]
        minimum = float('inf')
        for i in range(1,len(criticalPoint )):
            minimum = min(minimum,criticalPoint[i]-criticalPoint[i-1])
        return [minimum , maximum]
            