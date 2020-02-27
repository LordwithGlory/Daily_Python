class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Offer58:
    def judgetree(self,left,right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        elif left.val==right.val:
            return self.judgetree(left.left,right.right) and self.judgetree(left.right,right.left)
        else:
            return False

    def isSymmetrical(self, pRoot):
        if pRoot==None:
            return True
        if not pRoot.left and not pRoot.right:
            return True
        if not pRoot.left or not pRoot.right:
            return False
        return self.judgetree(pRoot.left,pRoot.right)
