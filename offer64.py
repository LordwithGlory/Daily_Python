class Offer64:
    def maxInWindows(self, num, size):
        res=[]
        numl=len(num)
        if not numl or not size or numl<size:
            return res
        slide=[]
        for n in num:
            slide.append(n)
            if len(slide)==size:
                res.append(max(slide))
                slide.pop(0)
        return res
         