class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Offer17:
    # 某个提交代码真滴 思路六批 贴一下 这递归的思路着实厉害
    # def HasSubtree(self, pRoot1, pRoot2):
    #     # write code here
    #     if not pRoot1 or not pRoot2:
    #         return False
    #     return self.is_subtree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
     
    # def is_subtree(self, A, B):
    #     if not B:
    #         return True
    #     if not A or A.val != B.val:
    #         return False
    #     return self.is_subtree(A.left,B.left) and self.is_subtree(A.right, B.right)
    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot1==None or pRoot2==None:
            return False
        q=[pRoot1]
        while len(q)!=0:
            treenode=q[0]
            if treenode.val==pRoot2.val:
                prtlist=[treenode]
                sonlist=[pRoot2]
                res=True
                while len(sonlist)!=0:
                    if prtlist[0]==None:
                        res=False
                        break
                    if sonlist[0].val==prtlist[0].val:
                        if sonlist[0].left!=None:
                            sonlist.append(sonlist[0].left)
                            prtlist.append(prtlist[0].left)
                        if sonlist[0].right!=None:
                            sonlist.append(sonlist[0].right)
                            prtlist.append(prtlist[0].right)
                        del sonlist[0]
                        del prtlist[0]
                    else:
                        res=False
                        break
                if res:
                    return True
            if q[0].left!=None:
                q.append(q[0].left)
            if q[0].right!=None:
                q.append(q[0].right)
            del q[0]
        return False