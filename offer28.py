class Offer28:
    def MoreThanHalfNum_Solution(self, numbers):
        # 最快的用了collections.Counter对于numbers进行排序
        numbers= sorted(numbers)
        nlen=len(numbers)
        res=0
        count=1
        for i in range(1,nlen):
            if numbers[i]==numbers[i-1]:
                count+=1
                if count*2>nlen:
                    return numbers[i]
            else:
                count=1
        if count*2>nlen:
            res=numbers[nlen-1]
        return res