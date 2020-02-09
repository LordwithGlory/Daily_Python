class Offer7:
    def Fibonacci(self, n):
        if n==0 or n>39:
            return 0
        if n<3:
            return 1
        a=1
        b=1
        c=0
        for _ in range(3,n+1):
            c=a+b
            a=b
            b=c
        return c