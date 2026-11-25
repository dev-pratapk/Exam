import sys; sys.path.insert(0,'.')
from papers import P, SKILL
from collections import defaultdict
papers=list(P)
# 1. frequency
freq=defaultdict(set); marks=defaultdict(int)
for p in papers:
    for u,q in P[p].items():
        for side in q.values():
            for c,m in side:
                s=SKILL[c]; freq[s].add(p); marks[s]+=m
print("SKILL FREQUENCY (papers out of %d, R21 papers out of 4, last seen)"%len(papers))
for s in sorted(freq,key=lambda s:(s[:2],-len(freq[s]))):
    if 'other' in s: continue
    r21=[p for p in freq[s] if 'R21' in p]; last=max(freq[s],key=papers.index)
    print(f"{len(freq[s]):2d}/14  R21 {len(r21)}/4  last={last[:6]}  avgmarks/paper={marks[s]/len(freq[s]):4.1f}  {s}")
def score(p,S):
    tot=0
    for u,q in P[p].items():
        tot+=max(sum(m for c,m in side if SKILL[c] in S) for side in q.values())
    return tot
skills=[s for s in freq if 'other' not in s]
# 2. greedy: maximise worst-paper score then average
S=[];print("\nGREEDY BACKTEST: add one skill at a time (Part B /80)")
while len(S)<len(skills):
    best=max((s for s in skills if s not in S),key=lambda s:(min(score(p,S+[s]) for p in papers),sum(score(p,S+[s]) for p in papers)))
    S.append(best); sc=[score(p,S) for p in papers]
    print(f"{len(S):2d}. +{best:62s} worst={min(sc):2d} avg={sum(sc)/len(sc):4.1f} R21worst={min(score(p,S) for p in papers if 'R21' in p)}")
