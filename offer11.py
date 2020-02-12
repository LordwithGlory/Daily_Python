class Offer11:
    def NumberOf1(self, n):
        is_navie=False
        if n<0:
            is_navie=True
            n=0-n
            n-=1
        thelen=0
        res=0
        while n!=0:
            thelen+=1
            if n%2!=0:
                res+=1
            n/=2
        if is_navie:
            return 32-res
        else:
            return res