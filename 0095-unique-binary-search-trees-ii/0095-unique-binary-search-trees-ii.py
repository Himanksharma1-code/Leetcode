class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []

        def build_trees(start, end):
            if start > end:
                return [None]

            all_trees = []
            for root_val in range(start, end + 1):
                left_trees = build_trees(start, root_val - 1)
                right_trees = build_trees(root_val + 1, end)

                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        all_trees.append(root)

            return all_trees

        return build_trees(1, n)