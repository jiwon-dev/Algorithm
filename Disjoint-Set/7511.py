import sys
input=sys.stdin.readline
# 10m 01s
def find(n):
    if p[n]<0: return n
    p[n]=find(p[n])
    return p[n]

def merge(a,b):
    a=find(a);b=find(b)
    if a==b: return
    p[b]=a
    
for i in range(int(input())):
    n,k=int(input()),int(input())
    p=[-1]*n
    for _ in range(k):
        a,b=map(int,input().split())
        merge(a,b)
    print(f'Scenario {i+1}:')
    for _ in range(int(input())):
        u,v=map(int,input().split())
        if find(u)==find(v): print(1)
        else: print(0)
    print()
    
