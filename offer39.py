class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Offer39:
    def IsBalanced_Solution(self, pRoot):
        # if pRoot==None:
        #     return True,0
        # lbool,lhigh=self.IsBalanced_Solution(pRoot.left)
        # rbool,rhigh=self.IsBalanced_Solution(pRoot.right)
        # if lbool and rbool and abs(lhigh-rhigh)<2:
        #     return True,max(lhigh,rhigh)+1
        # return False,0
        res,_=self.IsBalanced_Solution1(pRoot)
        return res

    def IsBalanced_Solution1(self,pRoot):
        if pRoot==None:
            return True,0
        lbool,lhigh=self.IsBalanced_Solution1(pRoot.left)
        rbool,rhigh=self.IsBalanced_Solution1(pRoot.right)
        if lbool and rbool and abs(lhigh-rhigh)<2:
            return True,max(lhigh,rhigh)+1
        return False,0

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.left.right.left=TreeNode(6)
o=Offer39()
print(o.IsBalanced_Solution(root))