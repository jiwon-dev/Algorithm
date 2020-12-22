import sys
input=sys.stdin.readline
# 19m 34s
# 사이클이 돈다는 말은 merge에서 a==b일 때와 같다
sys.setrecursionlimit(10**6)
def find(n):
    if p[n]<0: return n
    p[n]=find(p[n])
    return p[n]

def merge(a,b):
    a=find(a);b=find(b)
    if a==b: return True
    p[b]=a
    return False

n,m=map(int,input().split())
p=[-1]*n
for i in range(m):
    a,b=map(int,input().split())
    res=merge(a,b)
    if res:
        print(i+1)
        break
else: print(0)
