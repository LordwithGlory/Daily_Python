class Offer53:
    def isNumeric(self, s):
        #  最快的try: p = float(s)
        s=s.lower()
        count=0
        words=[]
        if 'e' in s:
            if s.count("e")>1:
                return False
            words=s.split('e')
            if not len(words[1]):
                return False
        else:
            words.append(s)
        for word in words:
            if '.' in word and count:
                return False
            beginpos=0
            count=1
            if word[0]=="+" or word[0]=='-':
                beginpos=1
            haspoint=False
            for pos in range(beginpos,len(word)):
                if word[pos]=='.' and not haspoint:
                    haspoint=True
                    if pos==len(word)-1:
                        return False
                    continue
                if not word[pos].isdigit():
                    return False
        return True

o=Offer53()
s="12E"
print(o.isNumeric(s))