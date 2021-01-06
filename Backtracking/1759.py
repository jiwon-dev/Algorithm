import sys
input=sys.stdin.readline
def sec(idx,s):
    print(s)
    if idx==C:
        mo=['a','e','i','o','u']
        cnt=0
        for v in mo: cnt+=s.count(v)
        if len(s)==L and cnt>=1 and len(s)-cnt>=2: print(s)
        return

    sec(idx+1,s+key[idx])
    sec(idx+1,s)
    
L,C=map(int,input().split())
key=input().split()
key.sort()
sec(0,"")

