import os
import sys

class Hello:
    hstr='Hello World'
    def output(self):
        print(self.hstr)
    def sysout(self):
        self.output()

hl=Hello()
hl.sysout()