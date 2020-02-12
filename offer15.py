class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Offer15:
    def ReverseList(self, pHead):
        res=None
        while pHead!=None:
            tmp=ListNode(pHead.val)
            tmp.next=res
            res=tmp
            pHead=pHead.next
        return res