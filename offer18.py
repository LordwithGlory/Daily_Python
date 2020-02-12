class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Offer19:
    def Mirror(self, root):
        # 学到一招骚操作
        # root.left,root.right = root.right,root.left
        if root==None:
            return root
        if root.left!=None:
            root.left=self.Mirror(root.left)
        if root.right!=None:
            root.right=self.Mirror(root.right)
        tmpnode=root.left
        root.left=root.right
        root.right=tmpnode
        return root