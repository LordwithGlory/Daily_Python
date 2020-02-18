class Offer27:
    def GetList(self,slist,hasviewd,restlen):
        mylen=len(slist)
        res=[]
        for i in range(mylen):
            if i and slist[i]==slist[i-1] and not hasviewd[i-1]:
                continue
            if hasviewd[i]:
                continue
            else:
                if restlen==1:
                    res.append(slist[i])
                    continue
                hasviewd[i]=True
                for one in self.GetList(slist,hasviewd,restlen-1):
                    one=slist[i]+one
                    res.append(one)
                hasviewd[i]=False
        return res
    def Permutation(self, ss):
        slist=list(ss)
        slist.sort()
        slen=len(slist)
        if not slen:
            return []
        hasviewd=[False]*slen
        return self.GetList(slist,hasviewd,slen)

offer=Offer27()
print(offer.Permutation("bacde"))