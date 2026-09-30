class Solution:
    def pathSum(self, root, targetSum):
        res = []

        def backtrack(node, remaining_sum, path):
            if not node:
                return

            path.append(node.val)

            if not node.left and not node.right and remaining_sum == node.val:
                res.append(list(path))
            else:
                backtrack(node.left, remaining_sum - node.val, path)
                backtrack(node.right, remaining_sum - node.val, path)

            path.pop()

        backtrack(root, targetSum, [])
        return res