class Offer32:
    def PrintMinNumber(self, numbers):
        # 最快的那个使用lamda表达式来进行排序
        strlist=[]
        res=""
        for num in numbers:
            strlist.append(str(num))
        strlist= sorted(strlist)
        while strlist:
            minpos=0
            for pos in range(1,len(strlist)):
                tmp1=strlist[minpos]+strlist[pos]
                tmp2=strlist[pos]+strlist[minpos]
                if tmp2<tmp1:
                    minpos=pos
                # tmp=strlist[minpos]
                # nowstr=strlist[pos]
                # if tmp==nowstr:
                #     continue
                # nowlen=len(nowstr)
                # tmplen=len(tmp)
                # j=k=0
                # while j<tmplen and k<nowlen:
                #     if tmp[j]!=nowstr[k]:
                #         break
                # if j==tmplen:
                #     j=0
                # if k==nowlen:
                #     k=0
                # if tmp[j]>nowstr[k]:
                #     minpos=pos
            res+=strlist[minpos]
            del strlist[minpos]
        return res

o=Offer32()
numbers=[21,23,2,211]
print(o.PrintMinNumber(numbers))