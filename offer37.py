class Offer37:
    def GetNumberOfK(self, data, k):
        # return data.count(k)
        bigger=False
        if not len(data):
            return 0
        if data[-1]>data[0]:
            bigger=True
        elif data[-1]==data[0]:
            if data[0]==k:
                return len(data)
            else:
                return 0
        if bigger:
            count=0
            for i in data:
                if i>k:
                    break
                elif i==k:
                    count+=1
            return count
        else:
            count=0
            for i in data:
                if i<k:
                    break
                elif i==k:
                    count+=1
            return count