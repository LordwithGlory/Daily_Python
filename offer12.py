class Offer12:
    def Power(self, base, exponent):
        is_naive=False
        if exponent<0:
            is_naive=True
            exponent*=-1
        if exponent==0:
            return 1
        res=1
        for _ in range(exponent):
            res*=base
        if is_naive:
            res=1/res
        return res