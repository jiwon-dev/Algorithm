import sys
input=sys.stdin.readline
# 1시간 이상
L,R=input().split()
ans=0
if len(L)==len(R):
    for i in range(len(L)):
        if L[i]==R[i]:
            if L[i]=='8':
                ans+=1
        else:
            break
print(L.count('8') if L==R else ans)

