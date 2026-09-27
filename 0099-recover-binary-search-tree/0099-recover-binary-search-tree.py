class Solution:
    def recoverTree(self, root):
        first = second = prev = None
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            if prev and curr.val < prev.val:
                if not first:
                    first = prev
                second = curr

            prev = curr
            curr = curr.right

        first.val, second.val = second.val, first.val