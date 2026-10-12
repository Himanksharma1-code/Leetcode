class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0

        left_height = 0
        node = root
        while node:
            left_height += 1
            node = node.left

        right_height = 0
        node = root
        while node:
            right_height += 1
            node = node.right

        if left_height == right_height:
            return (1 << left_height) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)