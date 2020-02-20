class Offer31:
    def NumberOf1Between1AndN_Solution(self, n):
        # 最快的那个真的是是个人
        # 个位百味慢慢分析
        base=0
        res=0
        if n%10:
            res+=1
        base=1
        rest=n%10
        n=int(n/10)
        pos=1
        while n:
            now=int(n%10)
            # 主要是还可能考虑到1这个特殊情况
            if now==1:
                res+=rest+1+base
            elif now:
                res+=pos+now*base
            pos*=10
            rest=now*pos+rest
            base=base*10+pos
            n=int(n/10)
        return res

o=Offer31()
print(o.NumberOf1Between1AndN_Solution(11))