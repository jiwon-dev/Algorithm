# 06m 
for _ in range(int(input())):
    S=input()
    if len(S)%2==1: print('No')
    else:
        alp=[0]*26
        for v in S:
            if not ('a'<=v<='z' or 'A'<=v<='Z'): continue
            tmp=v.lower()
            alp[ord(tmp)-ord('a')]+=1

        chk=True
        for i in range(26):
            if alp[i]!=alp[25-i]: chk=False; break
        if chk: print('Yes')
        else: print('No')
