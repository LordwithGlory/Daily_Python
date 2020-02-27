class Offer54:
    def __init__(self):
        # 在外面直接初始化可能有问题。。。
        self.once=[]
        self.more=[]

    def FirstAppearingOnce(self):
        if len(self.once):
            return self.once[0]
        else:
            return "#"
    def Insert(self, char):
        if char in self.once:
            self.once.remove(char)
            self.more.append(char)
        elif char in self.more:
            return
        else:
            self.once.append(char)

mystr="helloworld"
o=Offer54()
for c in mystr:
    o.Insert(c)
    print(o.FirstAppearingOnce())