class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Offer38:
    def TreeDepth(self, pRoot):
        if pRoot==None:
            return 0
        return 1+max(self.TreeDepth(pRoot.left),self.TreeDepth(pRoot.right))