class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Offer4:
    def reConstructBinaryTree(self,pre,tin):
        prelen=len(pre)
        if prelen==0:
            return None
        root=TreeNode(pre[0])
        prepos=1
        nowode=root
        while prepos<prelen:
            formernum=pre[prepos-1]
            nownum=pre[prepos]
            if tin.index(nownum)<tin.index(formernum):
                # 判断是在左子树上，如果前序相邻并且中序遍历位置在前
                nowode.left=TreeNode(nownum)
                nowode=nowode.left
            else:
                # 如果不是在左子树上那么就是在右子树或者父母节电以及祖先节点右子树上
                nowode=root
                nowindex=tin.index(nownum)
                while True:
                    nodeindex=tin.index(nowode.val)
                    # 开始因为这个地方大小问题所以蒙蔽了
                    if nowindex<nodeindex:
                        # if nowode.left==None:
                        #     nowode.left=TreeNode(nownum)
                        #     nowode=nowode.left
                        #     break
                        nowode=nowode.left
                        continue
                    elif nodeindex<nowindex:
                        if nowode.right==None:
                            nowode.right=TreeNode(nownum)
                            nowode=nowode.right
                            break
                        nowode=nowode.right
                        continue
            prepos=prepos+1
        return root

o4=Offer4()
o4.reConstructBinaryTree([1,2,3,4,5,6,7],[3,2,4,1,6,5,7])