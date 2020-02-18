class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Offer26:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
        if pRootOfTree.left:
            lefttree=self.Convert(pRootOfTree.left)
            while lefttree.right:
                lefttree=lefttree.right
            lefttree.right=pRootOfTree
            pRootOfTree.left=lefttree
        if pRootOfTree.right:
            righttree=self.Convert(pRootOfTree.right)
            pRootOfTree.right=righttree
            righttree.left=pRootOfTree
        while pRootOfTree.left:
            pRootOfTree=pRootOfTree.left
        return pRootOfTree