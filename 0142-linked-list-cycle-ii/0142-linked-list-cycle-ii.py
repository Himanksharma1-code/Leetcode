class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                finder = head
                while finder != slow:
                    finder = finder.next
                    slow = slow.next
                return finder

        return None