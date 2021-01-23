import sys
input=sys.stdin.readline
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())

def cross(x1,y1,x2,y2):
    return x1*y2-x2*y1

a,b=x2-x1,y2-y1
c,d=x3-x2,y3-y2
res=cross(a,b,c,d)
if res>0: print(1)
elif res==0: print(0)
else: print(-1)
