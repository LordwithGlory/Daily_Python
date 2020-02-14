class Offer20:
    mylist=[]
    minpos=0
    def push(self,node):
        self.mylist.append(node)
        if len(self.mylist)!=1:
            if node<self.mylist[self.minpos]:
                self.minpos=len(self.mylist)-1
    
    def pop(self):
        if len(self.mylist)==0:
            return None
        # 变量名还是别相似的好否则分不清
        if self.minpos==len(self.mylist)-1:
            self.minpos=0
            for i in range(1,len(self.mylist)-1):
                if self.mylist[i]<self.mylist[self.minpos]:
                    self.minpos=i
        return self.mylist.pop()
    
    def min(self):
        if len(self.mylist)==0:
            return None
        return self.mylist[self.minpos]

o20=Offer20()
o20.push(3)
o20.min()
o20.push(4)
o20.min()
o20.push(2)
o20.min()
o20.pop()
o20.min()
o20.pop()
o20.min()
o20.pop()
o20.min()
o20.push(0)
o20.min()