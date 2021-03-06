# 9m
import sys
dic={'Re':0,'Pt':0,'Cc':0,'Ea':0,'Tb':0,'Cm':0,'Ex':0}
hap=0
for S in sys.stdin:
    # 한 줄씩 S에 입력받음
    for v in S.split():
        # S를 split하여 한 일들을 추려냄
        hap+=1
        if v not in dic: continue
        dic[v]+=1
        # dic에 한 일에 대한 횟수 증가
for a,b in dic.items(): print(a,b,'%.2f'%(b/hap))
print(f'Total {hap} 1.00')
        
