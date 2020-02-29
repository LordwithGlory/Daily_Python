class Offer63:
    def __init__(self):
        self.thelist=[]

    def Insert(self, num):
        # 这个不必须
        num=float(num)
        if not len(self.thelist):
            self.thelist.append(num)
            return
        left=0
        right=len(self.thelist)-1
        while left<right:
            mid = int((left+right)/2)
            if self.thelist[mid]>num:
                right=mid-1
            else:
                left=mid+1
        if left==right:
            if num>self.thelist[left]:
                self.thelist.insert(left+1,num)
            else:
                self.thelist.insert(left,num)
        else:
            self.thelist.insert(right,num)
        return self.GetMedian()

    def GetMedian(self):
        tlen=len(self.thelist)
        if not tlen:
            return None
        if tlen%2:
            # //符号可以代表整数除
            return self.thelist[int(tlen/2)]
        else:
            one=int(tlen/2)
            two=one-1
            # 可以把这个地方替换为除以2.0
            return (self.thelist[one]+self.thelist[two])/2

o=Offer63()
print(o.Insert(5))
print(o.Insert(2))