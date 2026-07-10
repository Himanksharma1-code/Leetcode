class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0, head)
        prev = dummy
        while True:
            node = prev
            for _ in range(k):
                node = node.next
                if not node:
                    return dummy.next
            nxt = node.next
           
            curr, prev_sub = prev.next, nxt
            for _ in range(k):
                curr.next, prev_sub, curr = prev_sub, curr, curr.next
            temp = prev.next
            prev.next = prev_sub
            prev = temp