class Offer30:
    def FindGreatestSumOfSubArray(self, array):
        alen=len(array)
        res=array[0]
        for i in range(1,alen):
            if array[i-1]>0:
                array[i]+=array[i-1]
            if array[i]>res:
                res=array[i]
        return res