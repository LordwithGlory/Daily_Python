class Offer43:
    def LeftRotateString(self, s, n):
        if not s:
            return s
        n%=len(s)
        if n:
            tmp1=s[:n]
            tmp2=s[n:]
            s=tmp2+tmp1
        return s