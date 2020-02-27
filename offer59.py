class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Offer59:
    # 最快那个用的双向连标可还行==
    def viewtree(self,pRoot,floor,res):
        if len(res)<=floor or not floor:
            res.append([])
        res[floor].append(pRoot.val)
        if pRoot.left:
            self.viewtree(pRoot.left,floor+1,res)
        if pRoot.right:
            self.viewtree(pRoot.right,floor+1,res)

    def Print(self, pRoot):
        res=[]
        if not pRoot:
            return res
        self.viewtree(pRoot,0,res)
        count =0 
        for mylist in res:
            if count%2:
                mylist.reverse()
            count+=1
        return res