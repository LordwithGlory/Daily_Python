class Offer19:
    def printMatrix(self, matrix):
        res=[]
        rowlen=len(matrix)
        if rowlen==0:
            return res
        collen=len(matrix[0])
        if collen==0:
            return res
        hasviewed =[[False for _ in range(collen)]for _ in range(rowlen)]
        stepward=0
        
        x=y=0
        while len(res)<rowlen*collen:
            if hasviewed[x][y]==False:
                res.append(matrix[x][y])
            hasviewed[x][y]=True
            if stepward==0 and y+1<collen and hasviewed[x][y+1]==False:
                y=y+1
                continue
            if stepward==0:
                stepward=1
            if stepward==1 and x+1<rowlen and hasviewed[x+1][y]==False:
                x=x+1
                continue
            if stepward==1:
                stepward=2
            if stepward==2 and x>=1 and hasviewed[x-1][y]==False:
                x=x-1
                continue
            if stepward==2:
                stepward=3
            if stepward==3 and y>=1 and hasviewed[x][y-1]==False:
                y=y-1
                continue
            if stepward==3:
                stepward=0
                continue
        return res
            