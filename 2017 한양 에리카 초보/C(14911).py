import sys
input=sys.stdin.readline
# 7m
s=list(map(int,input().split()))
s.sort()
n=int(input())
res=[]
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i]>s[j]: continue
        if s[i]+s[j]==n:
            if (s[j],s[i]) in res or (s[i],s[j]) in res: continue
            res.append((s[i],s[j]))
for a,b in res: print(a,b)
print(len(res))
