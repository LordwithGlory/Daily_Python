class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Offer61:
    def __init__(self):
        self.fomer=""
        self.mid=""

    def Serialize(self, root):
        if not root:
            return None
        self.fomer+=str(root.val)+"!"
        if root.left:
            self.Serialize(root.left)
        self.mid+=str(root.val)+"!"
        if root.right:
            self.Serialize(root.right)
        return self.fomer+"#"+self.mid

    def ConstructTree(self, before, mid):
        if not len(before):
            return None
        theval=before[0]
        midpos=mid.index(theval)
        root=TreeNode(int(theval))
        root.left=self.ConstructTree(before[1:midpos+1],mid[:midpos])
        root.right=self.ConstructTree(before[midpos+1:],mid[midpos+1:])
        return root

    def Deserialize(self, s):
        if not s:
            return None
        befores,afters=s.split("#")
        before=befores.split("!")
        mid=afters.split("!")
        before.pop()
        mid.pop()
        root=self.ConstructTree(before,mid)
        return root

o=Offer61()
root=TreeNode(8)
root.left=TreeNode(6)
root.right=TreeNode(10)
root.left.left=TreeNode(5)
root.left.right=TreeNode(7)
root.right.left=TreeNode(9)
root.right.right=TreeNode(11)
o.Deserialize(o.Serialize(root))