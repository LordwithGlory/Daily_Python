class Offer46:
    def LastRemaining_Solution(self, n, m):
        # 居然可直接使用pop函数
        if not n:
            return -1
        children=[i for i in range(n)]
        delpos=0
        while len(children)>1:
            clen=len(children)
            delpos+=m-1
            delpos%=clen
            del children[delpos]
        return children[0]