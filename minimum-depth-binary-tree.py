# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        if not root: 
            return 0
        d = map(self.minDepth, (root.left, root.right)) #map(function_to_apply, list_of_inputs)
        return 1 + (min(d) or max(d))