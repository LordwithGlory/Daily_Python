class Offer48:
    def Add(self, num1, num2):
        # return sum([num1,num2])
        if not num1:
            return num2
        elif not num2:
            return num1
        while num2:
            num1,num2=num1|num2,num1&num2
            num2<<1
        return num1