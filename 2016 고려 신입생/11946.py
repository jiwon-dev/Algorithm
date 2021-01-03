import sys
input=sys.stdin.readline
# 25m
n,m,q=map(int,input().split())

chk=[[False]*(m+1) for _ in range(n+1)]
cnt=[[0]*(m+1) for _ in range(n+1)]
ans=[[i,0,0] for i in range(n+1)]
for _ in range(q):
    time,team,pro,res=input().split()
    time=int(time);team=int(team);pro=int(pro)
    if chk[team][pro]: continue
    elif res=='AC':
        chk[team][pro]=True
        ans[team][1]+=1
        ans[team][2]+=cnt[team][pro]*20+time
    else: cnt[team][pro]+=1
ans=ans[1:]
ans.sort(key=lambda x:[-x[1],x[2],x[0]])
for a,b,c in ans: print(a,b,c)
