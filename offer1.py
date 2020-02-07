class ofer1:
    def find(self, target, array):
        # 行数
        rowlen=len(array)
        # array是[[]]的时候 rowlen是1 collen是0
        if rowlen==0:
            return False
        # 列数
        collen=len(array[0])
        nowrow=0
        if collen==0:
            return False
        while nowrow<rowlen:
            if array[nowrow][0]<=target and array[nowrow][collen-1]>=target:
                left=0
                right=collen-1
                while left<=right:
                    mid = int((left+right)/2)
                    if array[nowrow][mid]==target:
                        return True
                    elif array[nowrow][mid]>target:
                        right=mid-1
                    elif array[nowrow][mid]<target:
                        left=mid+1
                nowrow=nowrow+1
            else:
                nowrow=nowrow+1
                continue
        return False

o1= ofer1()
print(o1.find(16,[[]]))