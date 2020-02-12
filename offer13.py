class Offer13:
    def reOrderArray(self, array):
        # 最快的那个用了双向队列 六批
        # 最后使用list()方法转换
        lens=len(array)
        swappos=0
        for scanpos in range(lens):
            thenum=array[scanpos]
            if thenum%2==0:
                continue
            else:
                if swappos!=scanpos:
                    del array[scanpos]
                    # insert这个方法就很重要
                    array.insert(swappos,thenum)
                    swappos+=1
                else:
                    swappos+=1
        return array