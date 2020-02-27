class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Offer56:
    def deleteDuplication(self, pHead):
        if not pHead:
            return None
        res=ListNode(pHead.val-1)
        res.next=pHead
        former=res
        while pHead:
            if pHead.next:
                if pHead.next.val!=pHead.val:
                    former.next=pHead
                    former=former.next
                else:
                    old=pHead.val
                    pHead=pHead.next
                    while pHead:
                        if old!=pHead.val:
                            break
                        pHead=pHead.next
                    if not pHead:
                        former.next=None
                        break
                    continue
            else:
                former.next=pHead
            pHead=pHead.next
        return res.next