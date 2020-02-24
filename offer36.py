class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Offer36:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # 俺觉得这个题目应该有奇思妙想
        # emmm奇思妙想就是先让大家长度一样 机智鸭
        pHead1_copy=pHead1
        plone=[]
        while pHead1:
            plone.append(pHead1.val)
            pHead1=pHead1.next
        pltwo=[]
        while pHead2:
            pltwo.append(pHead2.val)
            pHead2=pHead2.next
        if  not len(plone) or not len(pltwo):
            return None
        if plone[-1]!=pltwo[-1]:
            return None
        thelen=min(len(plone),len(pltwo))
        for i in range(1,thelen+1):
            if plone[-i]!=pltwo[-i]:
                thepos=len(plone)-i
                while thepos>=0:
                    thepos=thepos-1
                    pHead1_copy=pHead1_copy.next
                return pHead1_copy
            if i==thelen:
                thepos=len(plone)-thelen
                while thepos:
                    pHead1_copy=pHead1_copy.next
                    thepos-=1
                return pHead1_copy
        return None
