import sys
input=sys.stdin.readline
# 13m 38s
n,m=map(int,input().split())
ans=0
q=[]
for _ in range(n):
    p,l=map(int,input().split())
    s=list(map(int,input().split()))
    s.sort(reverse=True)
    # 각각의 마일리지를 내림차순으로 정렬한다.
    # p<l(수강인원이 신청한 사람 수 보다 많을 경우)이면 1 마일리지만 넣어도 수강 가능하므로 1 추가
    # 아니면, l번째의 마일리지만 넣어도 수강 가능하므로 s[l-1]을 추가
    if p<l: q.append(1)
    else: q.append(s[l-1])
q.sort()
# 최대한 많은 과목을 들어야하므로 오름차순으로 정렬
total=0
for v in q:
    total+=v
    if total<=m: ans+=1
    # 주어진 마일리지 이하면 ans+=1
print(ans)
    
        
