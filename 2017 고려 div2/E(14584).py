import sys
input=sys.stdin.readline
# 31m
s=input().rstrip()
N=int(input())
W=[input().rstrip() for _ in range(N)]
d=[]
for i in range(26):
    tmp=''
    for v in s:
        stan=ord(v)+i
        if stan>ord('z'): tmp+=chr(stan-ord('z')+ord('a')-1)
        else: tmp+=chr(stan)
    for word in W:
        if tmp.count(word)>0:
            print(tmp)
            sys.exit()
