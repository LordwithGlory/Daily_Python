class Offer8:
    def jumpFloor(self, number):
        res=[]
        if number<2:
            return 1
        elif number==2:
            return 2
        res.insert(0,1)
        res.insert(0,2)
        for _ in range(number-2):
            nextinsert=res[0]+res[1]
            res.insert(0,nextinsert)
        return res[0]

o8=Offer8()
print(o8.jumpFloor(3))