class Offer52:
    mymap={}
    def match(self, s, pattern):
        if self.mymap.get(s+" "+pattern):
            return self.mymap[s+" "+pattern]
        if not s and not pattern:
            return True
        if not pattern:
            return False
        res=False
        if len(pattern)>1 and pattern[1]=="*":
            if not s:
                res=self.match(s,pattern[2:])
            elif s[0]==pattern[0] or pattern[0]=='.':
                res=self.match(s[1:len(s)],pattern[2:]) or self.match(s[1:],pattern) or self.match(s,pattern[2:])
            else:
                res=self.match(s,pattern[2:len(pattern)])
        else:
            if not s:
                return False
            if s[0]==pattern[0] or pattern[0]=='.':
                res=self.match(s[1:],pattern[1:])
            else:
                res=False
        self.mymap[s+" "+pattern]=res
        return res

s=""
p=".*"
o=Offer52()
print(o.match(s,p))