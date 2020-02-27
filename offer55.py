class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Offer55:
    def EntryNodeOfLoop(self, pHead):
        mylist=[]
        while pHead:
            if pHead in mylist:
                return pHead
            mylist.append(pHead)
            pHead=pHead.next
        return None