class Offer45:
    def IsContinuous(self, numbers):
        # 快的好像都是先排序的
        if len(numbers)<5:
            return False
        minnum=14
        maxnum=-1
        count=0
        for num in numbers:
            if not num:
                count+=1
                continue 
            if numbers.count(num)>1:
                return False
            if minnum>num:
                minnum=num
            if maxnum<num:
                maxnum=num
        need=maxnum-minnum+1-(len(numbers)-count)
        if need<=count:
            return True
        return False
