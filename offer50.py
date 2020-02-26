class Offer50:
    def duplicate(self, numbers, duplication):
        # 最快的使用的是collections.Counter
        res=False
        for num in numbers:
            if num in duplication:
                duplication[0]=num
                res=True
                break
            duplication.append(num)
        return res