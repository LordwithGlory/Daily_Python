class Offer23:
    def VerifySquenceOfBST(self, sequence):
        if len(sequence)==0:
            return False
        if len(sequence)<3:
            return True
        fewer=-1
        for i in range(len(sequence)):
            if fewer==-1 and sequence[i]>sequence[-1]:
                fewer=i
            if fewer!=-1 and sequence[i]<sequence[-1]:
                return False
        first=self.VerifySquenceOfBST(sequence[:fewer])
        secnd=self.VerifySquenceOfBST(sequence[fewer:len(sequence)-1])
        if fewer!=0 and fewer!=-1:
            return  first and secnd
        if fewer==0:
            return secnd
        if fewer==-1:
            return first