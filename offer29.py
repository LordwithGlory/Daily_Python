class Offer29:
    def GetLeastNumbers_Solution(self, tinput, k):    
        # 简直是狗lz手写快拍都不行还要按照顺序     
        tinput=sorted(tinput)
        if k>len(tinput) or not k:
            return []   
        else:
            return tinput[:k]
        # fewer=[]
        # biger=[]
        # if k==0:
        #     return fewer
        # elif k>len(tinput):
        #     return biger
        # elif k==len(tinput):
        #     return tinput
        # intnl=tinput[0]
        # lens=len(tinput)
        # for i in range(1,lens):
        #     if tinput[i]<intnl:
        #         fewer.append(tinput[i])
        #     else:
        #         biger.append(tinput[i])
        # flen=len(fewer)
        # if flen==k:
        #     return fewer
        # elif flen<k:
        #     fewer.append(intnl)
        #     for one in self.GetLeastNumbers_Solution(biger,k-1-flen):
        #         fewer.append(one)
        # else:
        #     fewer=self.GetLeastNumbers_Solution(fewer,k)
        # return fewer