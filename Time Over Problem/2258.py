import sys
input=sys.stdin.readline
# 1시간 이상
N,M=map(int,input().split())
D=[list(map(int,input().split())) for _ in range(N)]
D.sort(key=lambda x:[x[1],-x[0]])
# 가격 오름차순 정렬, 가격이 같다면 무게가 무거운 순으로 정렬
# 무거운 순으로 정렬하는 이유:같은 가격이라면 무거운 무게를 사야 최솟값이 나오기 때문
ans=float('inf');price=0;weight=0;max_value=0
# 정답, 지불해야하는 가격(누적되거나 갱신됨), 누적 무게, 이전에 나온 최대 가격

for w,p in D:
    if p>max_value:
        # 가격이 최대 가격보다 크면 이전에 나왔던 가격이 작은 고기는 모두 살 수 있으므로 price를 p로 갱신
        max_value=p
        # 최대 가격 갱신
        price=p
        # 지불해야하는 가격 갱신
    else:
        # 최대 가격보다 작으면 price를 계속 누적해서 더함
        price+=p
    weight+=w
    # 사는 것의 제한은 없으니 weight는 계속 더해감
    if w>=M:
        # 현재 무게가 목표 무게 이상이면 ans=min(ans,p)
        ans=min(ans,p)
    if weight>=M:
        # 누적 무게가 M 이상이면 ans를 ans와 price 중 최솟값으로 갱신
        ans=min(ans,price)
print(-1 if ans==float('inf') else ans)
# ans가 한번도 갱신되지 않았다면 목표 무게를 넘지 못하는 것이므로 -1 출력 아니면 ans 출력
