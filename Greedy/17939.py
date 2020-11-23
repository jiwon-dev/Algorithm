import sys
input=sys.stdin.readline
# 06m 18s
# 뒤집은 뒤에 판매할 날(max_value)을 선택해서 그 날보다 가격이 작은 날이 나오면 판매할 날에 파는 방식
# 가격이 큰 날이 나오면 판매할 날을 갱신
N=int(input())
C=list(map(int,input().split()))[::-1]
ans=0
max_value=C[0]
for p in C[1:]:
    if max_value<=p: max_value=p
    else: ans+=max_value-p
print(ans)
