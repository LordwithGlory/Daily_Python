class Offer21:
    def IsPopOrder(self, pushV, popV):
        thelist=[]
        for i in range(len(pushV)):
            # 为什么不直接用 i in pushV
            thelist.append(pushV[i])
            # 我为什么不用-1来锁定最后一个呢
            while thelist[len(thelist)-1]==popV[0]:
                thelist.pop()
                del popV[0]
                if len(thelist)==0:
                    break
        if len(thelist)==0:
            return True
        return False
        # for i in range(len(pushV)):
        #     # i为什么不能变化，是真滴憨批
        #     if pushV[i]==popV[0]:
        #         del pushV[i]
        #         del popV[0]
        #         tmp= i-1
        #         while tmp>=0:
        #             if pushV[tmp]==popV[0]:
        #                 del pushV[tmp]
        #                 del popV[0]
        #                 tmp-=1
        #             else:
        #                 break
        #         i=i-1
        #     else:
        #         continue
        # if len(pushV)==0:
        #     return True
        # else:
        #     return False

o=Offer21()
print(o.IsPopOrder([1,2,3,4,5],[4,5,3,2,1]))