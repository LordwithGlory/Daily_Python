class Offer10:
    def rectCover(self, number):
        a=1
        b=2
        c=2
        if number==1:
            return 1
        elif number==0:
            return 0
        for _ in range(number-2):
            c=a+b
            a=b
            b=c
        return c