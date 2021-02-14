import sys
input=sys.stdin.readline
# 13m
N,K=map(int,input().split())
S=list(map(int,input().split()))
T=list(map(int,input().split()))
res=[]
for i in range(len(S)):
    for j in range(len(T)):
        res.append((j,S[i]*T[j]))
res.sort(key=lambda x:-x[1])
tmp=[]
for i,v in res:
    if i in tmp: continue
    if len(tmp)==K: print(v); break
    tmp.append(i)
