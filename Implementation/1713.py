import sys
input=sys.stdin.readline
# 30m 15s
# 정렬을 이용
pic=[]
N=int(input())
M=int(input())
S=list(map(int,input().split()))

# (시기, 추천받은횟수, 번호)
for i in range(M):
    # i를 시기로
    chk=False
    # 똑같은 번호가 있을 경우 True
    for j in range(len(pic)):
        if pic[j][2]==S[i]:
            pic[j][1]+=1
            chk=True
            break
    if chk: continue
    if len(pic)==N:
        pic.sort(key=lambda x:[x[1],x[0]])
        # 추천 받은 횟수, 시기 순으로 오름차순 정렬
        pic[0]=[i,1,S[i]]
        # 정렬 후, 사진틀의 제일 앞에 현재의 사진이 들어감
    else: pic.append([i,1,S[i]])
pic.sort(key=lambda x:x[2])
for c,v,n in pic: print(n,end=' ')
