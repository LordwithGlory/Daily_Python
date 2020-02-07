class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class Offer3:
    def printListFromTailToHead(self, listNode):
        res=[]
        while listNode!=None:
            res.insert(0,listNode.val)
            listNode=listNode.next
        return res