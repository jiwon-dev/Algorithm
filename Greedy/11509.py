import sys
input=sys.stdin.readline
# 58m 15s
N=int(input())
H=list(map(int,input().split()))
B=[0]*1000001
# i 높이의 풍선의 개수를 담는 리스트
ans=0
for v in H:
    if B[v+1]>0: B[v+1]-=1
    # v+1인 풍선이 있으면 터트림
    else: ans+=1
    # 없으면 화살을 추가해야하므로 ans+=1
    B[v]+=1
    # v인 풍선의 개수 늘림
print(ans)
