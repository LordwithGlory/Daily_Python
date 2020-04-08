import sys


mydirc=(0,1,5,8,7,2,9,4,3,6)
cases=int(sys.stdin.readline().strip())
for i in range(cases):
    num=sys.stdin.readline().strip()
    left=0
    right=len(num)-1
    res=True
    while left<right:
        if mydirc[int(num[left])]!=int(num[right]):
            res=False
            break
        left+=1
        right-=1
    if res:
        print("Yes")
    else:
        print("No")