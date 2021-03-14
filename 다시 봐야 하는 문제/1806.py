import sys
input=sys.stdin.readline
# 35m
N,S=map(int,input().split())
seq=list(map(int,input().split()))
s,e,hap=0,0,0
ans=float('inf')

while True:
    if hap>=S: hap-=seq[s]; s+=1; ans=min(ans,e-s+1)
    # hap>=S이면 s를 1 늘려서 다음 수에서 e까지의 합을 봐야함
    # 조건에 만족하므로 ans를 갱신
    elif e==N: break
    # hap<S이고 e==N(끝)이면 s에 상관없이 조건에 만족하는 구간은 없으니 break
    else: hap+=seq[e]; e+=1
    # hap<S이면 e를 1 늘려서 구간을 늘려 조건에 맞는지 확인해야함
print(0 if ans==float('inf') else ans)
