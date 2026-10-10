from collections import deque

class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        
        res = []
        queue = deque([root])
        
        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                if i == level_length - 1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return res