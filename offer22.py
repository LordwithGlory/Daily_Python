class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Offer22:
    def PrintFromTopToBottom(self, root):
        res=[]
        # python 0 和 None都可以进行判断作为bool真滴好啊
        if root==None:
            return res
        mylist=[root]
        while len(mylist):
            # 取值锁定这个操作限制速度
            if mylist[0].left:
                mylist.append(mylist[0].left)
            if mylist[0].right:
                mylist.append(mylist[0].right)
            res.append(mylist[0].val)
            del mylist[0]
        return res