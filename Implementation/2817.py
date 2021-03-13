# 23m
X,N=int(input()),int(input())
staff=[]
for _ in range(N):
    a,b=input().split()
    b=int(b)
    if b<X*0.05: N-=1; continue
    # 핵심
    # 5%미만인 스태프는 빼야하므로 N-=1을 해줘야 뒤에서 인덱스 에러가 뜨지 않음
    staff.append((a,b))
staff.sort(key=lambda x:x[0])

ans=[0]*N
tmp=[]
for i,(a,b) in enumerate(staff):
    for j in range(1,15): tmp.append((b/j,i))
tmp.sort(key=lambda x:-x[0])
for i in range(14): ans[tmp[i][1]]+=1
for j in range(N): print(staff[j][0],ans[j])

