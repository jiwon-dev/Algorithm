import sys
input=sys.stdin.readline
# 28m 37s
INF=float('inf')
atoi={};itoa={}
# 알파벳->인덱스, 인덱스->알파벳인 딕셔너리
for i in range(26):
    atoi[chr(ord('A')+i)]=i
    itoa[i]=chr(ord('A')+i)
for j in range(26):
    atoi[chr(ord('a')+j)]=j+26
    itoa[j+26]=chr(ord('a')+j)

D=[[INF]*52 for _ in range(52)]
# 모든 알파벳 대소문자가 들어갈 배열을 만듬
N=int(input())
for _ in range(N):
    a,b=input().rstrip().split(' => ')
    D[atoi[a]][atoi[b]]=0
    # a => b이면 D[a의 인덱스][b의 인덱스]=0으로 설정

for k in range(52):
    for i in range(52):
        for j in range(52):
            D[i][j]=min(D[i][j],D[i][k]+D[k][j])
# 플로이드 실행하면 A=>B인 참인 명제는 D[A의 인덱스][B의 인덱스]=0으로 설정됨

ans=[]
for i in range(52):
    for j in range(52):
        if i!=j and not D[i][j]:
            # 'A'=>'A'인 명제는 없으므로 제외
            ans.append(itoa[i]+' => '+itoa[j])
print(len(ans))
print(*ans,sep='\n')



