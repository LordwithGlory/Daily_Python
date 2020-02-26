class Offer42:
    def FindNumbersWithSum(self, array, tsum):
        res=[]
        # enumerate 建立索引进行感觉也不是快啊==
        for num in array:
            if tsum-num in array:
                res.append(num)
                res.append(tsum-num)
            break
        return res