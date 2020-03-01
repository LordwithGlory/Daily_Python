class Offer66:
    def getnum(self,num):
        count=0
        while num:
            count+=num%10
            num/=10
        return count

    def searchMarix(self,threshold,rows,cols,xc,yc,x,y,hasviewed):
        if xc+yc<=threshold:
            hasviewed[x][y]=True
        else:
            return 0
        count=1

        if y+1<cols and not hasviewed[x][y+1]:
            nyc=0
            if not (y+1)%10:
                nyc=self.getnum(y+1)
            else:
                nyc=yc+1
            count+=self.searchMarix(threshold,rows,cols,xc,nyc,x,y+1,hasviewed)

        if x+1<rows and not hasviewed[x+1][y]:
            nxc=0
            if not (x+1)%10:
                nxc=self.getnum(x+1)
            else:
                nxc=xc+1
            count+=self.searchMarix(threshold,rows,cols,nxc,yc,x+1,y,hasviewed)

        if y>1 and not hasviewed[x][y-1]:
            nyc=0
            if not y%10:
                nyc=self.getnum(y-1)
            else:
                nyc=yc-1
            count+=self.searchMarix(threshold,rows,cols,xc,nyc,x,y-1,hasviewed)

        if x>1 and not hasviewed[x-1][y]:
            nxc=0
            if not x%10:
                nxc=self.getnum(x-1)
            else:
                nxc=xc-1
            count+=self.searchMarix(threshold,rows,cols,nxc,yc,x-1,y,hasviewed)

        return count

            
    def movingCount(self, threshold, rows, cols):
        if  not rows or not cols:
            return 0
        hasviewed=[[False for i in range(cols)]for n in range(rows)]
        return self.searchMarix(threshold,rows,cols,0,0,0,0,hasviewed)
