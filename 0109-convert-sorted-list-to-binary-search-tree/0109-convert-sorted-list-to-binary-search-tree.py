class Solution:
    def sortedListToBST(self, head):
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        self.head = head

        def convert(left, right):
            if left > right:
                return None

            mid = (left + right) // 2

            left_child = convert(left, mid - 1)

            root = TreeNode(self.head.val)
            root.left = left_child

            self.head = self.head.next

            root.right = convert(mid + 1, right)

            return root

        return convert(0, length - 1)