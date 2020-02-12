class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Offer14:
    def FindKthToTail(self, head, k):
        hlen=0
        node=head
        while node!=None:
            node=node.next
            hlen+=1
        if hlen<k:
            return None
        hlen-=k
        for _ in range(hlen):
            head=head.next
        return head

o14=Offer14()
o14.FindKthToTail(ListNode(1),1)