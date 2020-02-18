class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Offer25:
    def Clone(self, pHead):
        # 最快的那个使用内置函数id()取内存地址着实有点东西
        randnode={}
        if pHead==None:
            return None
        res=RandomListNode(pHead.label)
        head=pHead
        tail=res
        pHead=pHead.next
        randnode[tail.label]=tail
        while pHead:
            tail.next=RandomListNode(pHead.label)
            tail=tail.next
            randnode[tail.label]=tail
            pHead=pHead.next
        tail=res
        while head:
            if head.random:
                tail.random=randnode[head.random.label]
            head=head.next
            tail=tail.next
        return res