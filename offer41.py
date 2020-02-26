class Offer41:
    def FindContinuousSequence(self, tsum):
        res=[]
        onelist=[]
        thesum=0
        for num in range(tsum):
            thesum+=num
            onelist.append(num)
            while thesum>tsum:
                thesum-=onelist.pop(0)
            if thesum==tsum:
                res.append(list(onelist))
            if num>tsum/2:
                break
        return res
