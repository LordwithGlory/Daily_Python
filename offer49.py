class Offer49:
    def StrToInt(self, s):
        if not s:
            return 0
        naive=False
        if s[0]=='-':
            naive=True
            s=s[1:]
        elif s[0]=='+':
            s=s[1:]
        numlist=['0','1','2','3','4','5','6','7','8','9']
        res=0
        if not s:
            return 0
        for n in s:
            if n not in numlist:
                return 0
            res*=10
            res+=numlist.index(n)
        if naive:
            res=0-res
        if res > 2147483647 or res < -2147483648:
            return 0
        return res