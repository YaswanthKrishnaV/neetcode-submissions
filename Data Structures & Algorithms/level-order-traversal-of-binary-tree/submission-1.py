# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # q = deque()
        # q.append(root)
        # res= []
        # while q:
        #     n = len(q)
        #     s= []
        #     for i in range(n):
        #         node = q.popleft()
        #         if node:
        #             s.append(node.val)
        #             q.append(node.left)
        #             q.append(node.right)
        #     if s:
        #         res.append(s)

        # return res
        res = []
        def dfs(node, depth):
            if not node:
                return None
            if len(res)==depth:
                res.append([])

            res[depth].append(node.val)
            dfs(node.left, depth+1)
            dfs(node.right,depth +1)

        dfs(root,0)
        return res
        