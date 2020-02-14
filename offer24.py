class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Offer24:
    def FindPath(self, root, expectNumber):
        # 我又想复杂了我以为是可以不是根结点==
        res=[]
        if not root:
            return res
        left=[]
        right=[]
        nownum=root.val
        if nownum>expectNumber:
            return res
        if nownum==expectNumber:
            if root.left or root.right:
                return res
            one=[nownum]
            res.append(one)
            return res
        if nownum<expectNumber:
            if root.left:
                left=self.FindPath(root.left,expectNumber-nownum)
            if root.right:
                right=self.FindPath(root.right,expectNumber-nownum)
        # 这个狗东西居然还是一个搜索二叉树==
        # 题目没写啊，难受
        # list1+list2可以形成新的list 并且 元素+list可以直接用 学到了
        # 用[]套一下就是列表 学到了
        for one in left:
            while right and len(one)<len(right[0]):
                res.append(right[0])
                del(right[0])
            res.append(one)
        for one in right:
            res.append(one)
        for one in res:
            one.insert(0,nownum)
        return res
        # 这个憨批代码写的是如何找到某个值==
        # res=[]
        # leftres=[]
        # rightres=[]
        # if root.left:
        #     leftres=self.FindPath(root.left,expectNumber)
        # if root.right:
        #     rightres=self.FindPath(root.right,expectNumber)
        # if len(leftres)==0 and len(rightres)==0:
        #     return None
        # for left in leftres:
        #     while rightres and len(left)<len(rightres[0]):
        #         res.append(rightres[0])
        #         del rightres[0]
        #     res.append(left)
        # for right in rightres:
        #     res.append(right)
        # for one in res:
        #     one.insert(0,expectNumber)
        # if expectNumber==root.val:
        #     onelist=[]
        #     onelist.append(expectNumber)
        #     res.append(onelist)
        # return res