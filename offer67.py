class Offer67:
    # 两种考虑一是从小往大计算然后每次都找这个长度最中间的1，2，3都知道，前四位是{ 0,1,2,3 }数组
    # 二是考虑有多少个2或者3 最大限度3但最后绝对不能剩余1（否则化为两个2）
    def moreCut(self, ropelen, base):
        res=1
        if ropelen<base*2:
            return ropelen
        for cut in range(base,ropelen//2+1):
            tmp=cut*self.moreCut(ropelen-cut,cut)
            if tmp>res:
                res=tmp
        return res

    def cutRope(self, number):
        if number<2:
            return 0
        if number==2:
            return 1
        maxres=0
        for lens in range(2,number//2+1):
            tmp=lens*self.moreCut(number-lens,lens)
            if tmp>maxres:
                return maxres
        return maxres