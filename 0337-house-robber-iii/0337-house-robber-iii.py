class Solution(object):
    def rob(self, root):
        def dfs(node):
            if not node:
                return (0, 0)

            left_rob, left_not = dfs(node.left)
            right_rob, right_not = dfs(node.right)

            rob_curr = node.val + left_not + right_not
            not_rob_curr = max(left_rob, left_not) + max(right_rob, right_not)

            return (rob_curr, not_rob_curr)

        return max(dfs(root))