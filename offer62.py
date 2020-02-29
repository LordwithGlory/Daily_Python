class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Offer62:
    def __init__(self):
        self.mylist=[]
    # def KthNode1(self,pRoot,thelist):
    #     res=None
    #     if pRoot.left:
    #         res=self.KthNode1(pRoot,thelist)
    #     if not res:
    #         return res
    #     thelist[0]-=1
    #     if not thelist[0]:
    #         return pRoot
    #     if pRoot.right:
    #         res=self.KthNode1(pRoot,thelist)
    #     return res
    # def KthNode2(self,pRoot,k):
    #     if not pRoot or not k:
    #         return None
    #     thelist=[k]
    #     self.KthNode1(pRoot,thelist)
    def KthNode(self, pRoot, k):
        if not pRoot or not k:
            return None
        if pRoot.left:
            self.KthNode(pRoot.left,k)
        self.mylist.append(pRoot)
        if len(self.mylist)>=k:
            return self.mylist[k-1]
        if pRoot.right:
            self.KthNode(pRoot.right,k)
        if len(self.mylist)>=k:
            return self.mylist[k-1]
        return None
        