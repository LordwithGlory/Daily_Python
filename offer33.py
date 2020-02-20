class Offer33:
    def GetUglyNumber_Solution(self, index):
        # 这个憨批和最后一个一样。。。，快的那个写的的确好
        # newUgly = min(uglyList[indexTwo]*2, uglyList[indexThree]*3, uglyList[indexFive]*5)
        # 用这个进行迭代获得下一个丑数，并通过这些获得
        if not index:
            return 0
        first=[2,3,5]
        res=[1]
        beginpos=0
        while len(res)<index*2:
            tmpres=res[beginpos:]
            nextpos=len(res)
            themax=res[len(res)-1]*5
            for num in tmpres:
                for i in first:
                    tmp=num*i
                    if tmp not in res:
                        res.append(tmp)
                    if tmp*5<themax:
                        tmpres.append(tmp)
            beginpos=nextpos
        res=sorted(res)
        return res[index-1]

        # 这个时间复杂度居然高
        # res=[1,2,3,4,5]
        # first=[2,3,5]
        # now=6
        # while len(res)<index:
        #     for num in first:
        #         if now%num:
        #             continue
        #         tmp=now/num
        #         if tmp in res:
        #             res.append(now)
        #             break
        #     now+=1
        # return res[index-1]

        # res=[1]
        # first=[2,3,5]
        # nopos=0
        # while len(res)<=index*2:
        #     for i in first:
        #         tmp=res[nopos]*i
        #         if tmp not in res:
        #             res.append(tmp)
        #     nopos+=1
        # res=sorted(res)
        # return res[index-1]