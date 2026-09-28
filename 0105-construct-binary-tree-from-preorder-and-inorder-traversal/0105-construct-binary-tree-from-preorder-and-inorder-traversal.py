class Solution:
    def buildTree(self, preorder, inorder):
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
        self.preorder_index = 0

        def array_to_tree(left, right):
            if left > right:
                return None

            root_value = preorder[self.preorder_index]
            root = TreeNode(root_value)
            self.preorder_index += 1

            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

            return root

        return array_to_tree(0, len(inorder) - 1)