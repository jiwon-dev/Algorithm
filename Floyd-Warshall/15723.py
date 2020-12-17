# 09m 29s
# 참은 0, 거짓은 INF
# [i][k]와 [k][j]가 참이면 [i][j]는 참임
INF=float('inf')
n=int(input())
alp={}
for i in range(26): alp[chr(ord('a')+i)]=i
D=[[INF]*26 for _ in range(26)]

for _ in range(n):
    a,b=input().split(' is ')
    D[alp[a]][alp[b]]=0

for k in range(26):
    for i in range(26):
        for j in range(26):
            if D[i][k]!=INF and D[i][k]==D[k][j]: D[i][j]=0

m=int(input())
for _ in range(m):
    a,b=input().split(' is ')
    print('F' if D[alp[a]][alp[b]]==INF else 'T')
