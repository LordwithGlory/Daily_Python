class offer65:
    def find(self,matrix,rows,cols,path,x,y):
        tmp=x*cols+y
        old=matrix[tmp]
        matrix=matrix[:tmp]+'0'+matrix[tmp+1:]
        path=path[1:]
        if not len(path):
            return True
        if y+1<cols and matrix[tmp+1]==path[0] and self.find(matrix,rows,cols,path,x,y+1):
            return True
        if x+1<rows and matrix[tmp+cols]==path[0] and self.find(matrix,rows,cols,path,x+1,y):
            return True
        if y and matrix[tmp-1]==path[0] and self.find(matrix,rows,cols,path,x,y-1):
            return True
        if x and matrix[tmp-cols]==path[0] and self.find(matrix,rows,cols,path,x-1,y):
            return True
        matrix=matrix[:tmp]+old+matrix[tmp+1:]
        return False
    
    def hasPath(self, matrix, rows, cols, path):
        if not cols or not rows or not len(path):
            return False   
        for pos in range(len(matrix)):
            if matrix[pos]==path[0] and self.find(matrix,rows,cols,path,pos//cols,pos%cols):
                return True
        return False

o=offer65()
o.hasPath('ABCESFCSADEE',3,4,'ABCCED')