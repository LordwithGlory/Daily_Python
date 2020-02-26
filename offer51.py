class Offer51:
    def multiply(self, A):
        B=[]
        B.insert(0,1)
        former=1
        for num in A[::-1]:
            former*=num
            B.insert(0,former)
        B.pop(0)
        former=1
        for i in range(len(B)):
            B[i]*=former
            former*=A[i]
        return B

o=Offer51()
A=[1,2,3,4,5]
print(o.multiply(A))