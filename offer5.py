class Offer5:
    list1=[]
    list2=[]
    def push(self, node):
        self.list1.append(node)

    def pop(self):
        # 发现一个厉害的想法就一旦pop就哦安段list2是否为空
        # 如果这个是空的那么就把list1全部入list2中，然后pop
        # 如果不为空则直接返回尾部元素
        # 比我这个省力一半啊。。。
        if self.list1==None:
            return None
        else:
            len1=len(self.list1)
            for i in range(len1-1):
                self.list2.append(self.list1.pop())
            thenum=self.list1.pop()
            for i in range(len1-1):
                self.list1.append(self.list2.pop())
            return thenum
            