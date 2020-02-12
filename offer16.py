class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Offer16:
    def Merge(self, pHead1, pHead2):
        if pHead2==None:
            return pHead1
        elif pHead1==None:
            return pHead2
        resone=pHead1
        restwo=pHead2
        if pHead1.val>pHead2.val:
            resone=pHead2
            restwo=pHead1
        res=resone
        while resone.next!=None:
            if restwo==None:
                break
            if resone.next.val>restwo.val:
                tmp=resone.next
                resone.next=restwo
                restwo=restwo.next
                resone.next.next=tmp
            resone=resone.next
        if restwo!=None:
            resone.next=restwo
        return res