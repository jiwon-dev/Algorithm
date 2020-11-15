import sys
input=sys.stdin.readline
# 07m 17s
n=int(input())
stick=sorted(map(int,input().split()))
# 길이를 오름차순으로 정렬해야 최소 비용을 구할 수 있음
total=sum(stick)
# 총 막대 길이를 줄여나가면서 ans를 구함
ans=0
# ans는 두 막대를 x,y라고 했을 때 x*y의 합
for v in stick:
    total-=v
    ans+=v*total
print(ans)
