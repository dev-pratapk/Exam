import sys; sys.path.insert(0,'.')
from papers import PAPERS, TOPICS
from collections import defaultdict
P=list(PAPERS)
def tops(t): return t.split('+')
def bc(p): return [q for q in PAPERS[p]['Q'] if q[0] in 'BC']
def score(p,S):
    tot=0; qs={q[1]:q for q in bc(p)}
    for k in ['11','12','13','14','15','16']:
        best=0
        for s in 'ab':
            q=qs.get(k+s)
            if not q: continue
            ts=tops(q[3]); m=q[4]; got=sum(m/len(ts) for t in ts if t in S); best=max(best,got)
        tot+=best
    return round(tot)
if __name__ == '__main__':
    pap=defaultdict(set); papB=defaultdict(set); papA=defaultdict(int)
    for p in P:
        for part,n,text,t,m in PAPERS[p]['Q']:
            for x in tops(t):
                pap[x].add(p)
                if part in 'BC': papB[x].add(p)
                else: papA[x]+=1
    print("TOPIC FREQUENCY (papers of 6 | R2021 papers of 3 | Part B/C papers | Part A count)")
    for x in sorted(TOPICS,key=lambda x:(TOPICS[x][0],-len(pap[x]))):
        r=sum('R17' not in p and 'R2017' not in PAPERS[p]['reg'] for p in pap[x])
        print(f"U{TOPICS[x][0]} {len(pap[x])}/6  R21 {r}/3  B/C {len(papB[x])}/6  A {papA[x]}  {TOPICS[x][1]}")
    print("not in syllabus:", {x:len(v) for x,v in pap.items() if x.startswith('x_')})
    skills=list(TOPICS); S=[]
    print("\nGREEDY (avg-maximising) Part B+C /80 ; per paper:", [p for p in P])
    while len(S)<16:
        b=max((s for s in skills if s not in S),key=lambda s:(sum(score(p,S+[s]) for p in P if 'CS3551' in PAPERS[p]['reg']),sum(score(p,S+[s]) for p in P)))
        S.append(b); sc=[score(p,S) for p in P]
        print(f"{len(S):2d} +{TOPICS[b][1][:60]:60s} R21={[score(p,S) for p in P if 'CS3551' in PAPERS[p]['reg']]} all={sc}")
