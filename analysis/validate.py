import sys; sys.path.insert(0,'.')
from papers import P, SKILL
from collections import defaultdict
papers=list(P); train=papers[:10]; test=papers[10:]
def score(p,S):
    return sum(max(sum(m for c,m in side if SKILL[c] in S) for side in q.values()) for q in P[p].values())
f=defaultdict(int)
for p in train:
    seen={SKILL[c] for q in P[p].values() for side in q.values() for c,m in side}
    for s in seen: f[s]+=1
rank=[s for s in sorted(f,key=lambda s:-f[s]) if 'other' not in s]
print("OUT-OF-SAMPLE: list built ONLY from 2016-2021 papers, tested on 2022-2024 R2021 papers (Part B /80)")
for k in (6,8,10,12,15):
    S=rank[:k]; print(f"top{k:2d} from old papers -> R21 scores {[score(p,S) for p in test]}")
print("top-12 list from old papers:"); [print("  ",f[s],s) for s in rank[:12]]
# expected-value greedy on all 14
S=[];skills=[s for s in {SKILL[c] for c in SKILL} if 'other' not in s]
print("\nAVERAGE-MAXIMISING ORDER (all 14 papers):")
for i in range(14):
    b=max((s for s in skills if s not in S),key=lambda s:sum(score(p,S+[s]) for p in papers)); S.append(b)
    sc=[score(p,S) for p in papers]; print(f"{i+1:2d}. {b:62s} avg={sum(sc)/14:4.1f} worst={min(sc)} R21={[score(p,S) for p in test]}")
print("\nper-paper with these 14:",{p[:6]:score(p,S) for p in papers})
