class Offer6:
    def minNumberInRotateArray(self, rotateArray):
        # 这个题目可以二分
        if len(rotateArray)==0:
            return 0
        res=rotateArray[0]
        for i in rotateArray:
            if i<res:
                res=i
        return res