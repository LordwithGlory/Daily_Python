class Offer9:
    def jumpFloorII(self, number):
        if number<2:
            return 1
        if number==2:
            return 2
        # 除了跳到其他地方还可以直接跳过去
        # 所以就是等于前面步数相加然后再加一
        res=4
        for _ in range(number-3):
            res*=2
        return res

o9=Offer9()
print(o9.jumpFloorII(3))