class Solution:
    def buildTree(self, inorder, postorder):
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}

        def array_to_tree(left, right):
            if left > right:
                return None

            root_value = postorder.pop()
            root = TreeNode(root_value)

            idx = inorder_index_map[root_value]

            root.right = array_to_tree(idx + 1, right)
            root.left = array_to_tree(left, idx - 1)

            return root

        return array_to_tree(0, len(inorder) - 1)