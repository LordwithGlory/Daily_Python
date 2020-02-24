class Offer40:
    def FindNumsAppearOnce(self, array):
        # 机智的操作是进行异或
        # 所有数字异或之后取第一个为1的数字，则该位中两个出现一次的数字i肯定不一样其他
        # 根据这位数字分为两部分（将这哥俩分开到两组），每个部分进行异或
        once=[]
        twice=[]
        more=[]
        for i in array:
            if i in once:
                once.remove(i)
                twice.append(i)
            elif i in twice:
                twice.remove(i)
                more.append(i)
            elif i in more:
                continue
            else:
                once.append(i)
        return once

array=[2,4,3,6,3,2,5,5]
o=Offer40()