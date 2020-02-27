class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Offer57:
    def GetNext(self, pNode):
        if pNode.right:
            pNode=pNode.right
            while pNode and pNode.left:
                pNode=pNode.left
        elif pNode.next:
            if pNode==pNode.next.right:
                while pNode.next:
                    if pNode==pNode.next.right:
                        pNode=pNode.next
                    else:
                        return pNode.next
                return pNode.next
            else:
                pNode=pNode.next
        else:
            pNode=None
        return pNode