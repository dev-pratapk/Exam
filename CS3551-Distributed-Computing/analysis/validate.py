import sys; sys.path.insert(0,'.')
from papers import PAPERS, TOPICS
from run import score, tops
from collections import defaultdict
P=list(PAPERS)
def rank(train, per_unit=2):
    f=defaultdict(float)
    for p in train:
        w=2 if 'CS3551' in PAPERS[p]['reg'] else 1
        seenB={x for q in PAPERS[p]['Q'] if q[0] in 'BC' for x in tops(q[3])}
        seenA={x for q in PAPERS[p]['Q'] if q[0]=='A' for x in tops(q[3])}
        for x in seenB: f[x]+=w
        for x in seenA: f[x]+=0.25*w
    S=[]
    for u in range(1,6):
        S+= sorted([x for x in TOPICS if TOPICS[x][0]==u], key=lambda x:-f[x])[:per_unit]
    return S
if __name__ == '__main__':
    for k in (2,3):
        print(f"LEAVE-ONE-OUT, top {k} topics per unit ({5*k} topics) chosen from the other 5 papers -> score on held-out paper (Part B+C /80)")
        for p in P:
            S=rank([q for q in P if q!=p],k); print(f"   {p:15s} {score(p,S):3d}/80")
    S=rank(P,2); print("\nFINAL top-2-per-unit list from all 6 papers:"); [print('  U%d'%TOPICS[x][0], TOPICS[x][1]) for x in S]
    S3=rank(P,3); print("third per unit:", [TOPICS[x][1] for x in S3 if x not in S])
    print("scores with final top-2 list:", {p:score(p,S) for p in P}); print("with top-3:", {p:score(p,S3) for p in P})
