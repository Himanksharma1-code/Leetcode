class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)
        curr = head

        while curr:
            prev = dummy
            nxt = curr.next

            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            curr.next = prev.next
            prev.next = curr
            curr = nxt

        return dummy.next