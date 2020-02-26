class Offer44:
    def ReverseSentence(self, s):
        tmps=s.strip()
        if not len(tmps):
            return s
        wordlist=s.split(" ")
        s=""
        for word in wordlist:
            if s:
                word+=" "
            s=word+s
        return s
