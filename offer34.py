class Offer34:
    def FirstNotRepeatingChar(self, s):
        # for i in s:
        #     if s.count(i)==1:
        #         return s.index(i)
        # return -1

        once=[]
        notonce=[]
        for i in s:
            if i in notonce:
                continue
            elif i in once:
                notonce.append(i)
                once.remove(i)
            else:
                once.append(i)
        if len(once):
            return s.index(once[0])
        else:
            return -1
        # 这个sort不起作用
        # s=sorted(s)
        # formerchar=s[0]
        # formernum=1
        # for i in range(1,len(s)):
        #     if s[i]==formerchar:
        #         formernum+=1
        #     else:
        #         if formernum==1:
        #             return i-1
        #         formerchar=s[i]
        #         formernum=1
        # if formernum==1:
        #     return len(s)-1
        # return -1