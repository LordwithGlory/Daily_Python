class Offer35:
    # 看得我脑壳疼
    def InversePairs(self, data):
        # 某个憨批把用例全跑出来改来。。。
        # return 24903408 if data[0]==26819 else 493330277 if data[0]==627126 else 988418660 if data[0]==74073 else 2519
        # 重新赋值后不会对原参数造成改变，但是append则会；，所以俺必须要传参数
        # python还有限制递归层数
        # 更改了递归层数说你超过限制hhh，真特么是一个神题目，python玩家告退
        if len(data)<2:
            return 0
        elif len(data)==2:
            if data[0]>data[1]:
                tmp=data[0]
                data[0]=data[1]
                data[1]=tmp
                return 1
            return 0
        datalen=len(data)
        half=int(datalen/2)
        datafom=data[:half]
        datalst=data[half:]
        data=[]
        one= self.InversePairs(datafom)
        two= self.InversePairs(datalst)
        nowpos=0
        res=one+two
        for i in datafom:
            while datalst and i>datalst[0]:
                data.append(datalst[0])
                res+=len(datafom)-nowpos
                del datalst[0]
            data.append(i)
            nowpos+=1
        for i in datalst:
            data.append(i)
        return res

        # orderdata= sorted(data)
        # res=0
        # for i in orderdata:
        #     res+=abs(orderdata.index(i)-data.index(i))
        # res/=2
        # res%=1000000007
        # return int(res)

o=Offer35()
num=[1,2,3,4,5,6,7,0]
# num=[364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]
print(o.InversePairs(num))
